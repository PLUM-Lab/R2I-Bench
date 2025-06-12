import re
import json
import pandas as pd
import os
from instance import *
import csv
category_scores = {}
summary_file = "results.csv"

os.makedirs("log", exist_ok=True)

for entry in category_subcategory_list:
    category = entry["category"]
    subcategory = entry["subcategory"]
    
    if category not in category_scores:
        category_scores[category] = []
    
    eval_csv_path = os.path.join("data", "evaluation", category, f"{subcategory}_eval.csv")
    prompt_csv_path = os.path.join("data", "prompts", category, f"{category}_{subcategory}.csv")
    
    try:
        eval_df = pd.read_csv(eval_csv_path)
        print(f"Processing {category}/{subcategory}: Found {len(eval_df)} evaluation questions")
        
        prompt_df = pd.read_csv(prompt_csv_path)
        print(f"Found {len(prompt_df)} prompt entries")
        
        grouped = eval_df.groupby('source_id')
        
        for source_id, group_df in grouped:
            question_list = []
            for _, row in group_df.iterrows():
                question_list.append({
                    "id": row["id"],
                    "question": row["question"],
                    "weight": row["weight"],
                    "criteria": row["evaluation_criteria"]
                })
            
            image_id = source_id
            image_path = os.path.join(
                "save", category, subcategory, 
                f"{category}_{subcategory}_{image_id}.png"
            )
            
            if not os.path.exists(image_path):
                print(f"Warning: Image {image_path} does not exist, skipping evaluation")
                continue
            
            prompt_row = prompt_df[prompt_df["id"] == source_id]
            
            if prompt_row.empty:
                print(f"Warning: Prompt with ID {source_id} not found, skipping evaluation")
                continue
            
            item_prompt = prompt_row.iloc[0]["Prompt"]
            
            q_list_str = "\n".join(
                [f"{q['id']}. {q['question']} \nCriteria: {q['criteria']}" 
                 for q in question_list]
            )
            
            final_prompt = PROMPT\
                .replace("[PROMPT]", item_prompt)\
                .replace("[QUESTION_LIST]", q_list_str)
            
            evaluation = get_llm_response(final_prompt, image_path)
            print(f"Evaluation result:\n{evaluation}")
            
            try:
                json_match = re.search(r'```json\n(.*?)\n```', evaluation, flags=re.DOTALL)
                if json_match:
                    json_str = json_match.group(1)
                else:
                    json_str = evaluation
                
                fixed_str = re.sub(r'[\x00-\x1f\x7f]', '', json_str)
                evaluation_dict = json.loads(fixed_str)
                
                above = 0
                under = 0
                
                for q in question_list:
                    q_id = str(q["id"])
                    if q_id in evaluation_dict:
                        score = float(evaluation_dict[q_id])
                        above += q["weight"] * score
                        under += q["weight"] * 1
                
                if under == 0:
                    final_score = 0.0
                else:
                    final_score = round(above / under, 2)
                
                print(f"Computed score: {final_score}")
                
                category_scores[category].append(final_score)

            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Error parsing evaluation result: {str(e)}")

    except FileNotFoundError as e:
        print(f"Error: File not found {e.filename}")
    except Exception as e:
        print(f"Error processing {category}/{subcategory}: {str(e)}")

with open(summary_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Average Score", "Data Instances Count"])
    
    for category, scores in category_scores.items():
        if scores:
            average_score = round(sum(scores) / len(scores), 2)
            count = len(scores)
        else:
            average_score = 0.0
            count = 0
        
        writer.writerow([category, average_score, count])
        print(f"Category {category}: Average score {average_score}, based on {count} data instances")

print("Evaluation process completed! Summary results saved to", summary_file)
