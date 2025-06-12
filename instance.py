API_KEY="fill your apikey here"
category_subcategory_list = [

    {"category": "commonsense", "subcategory": "social_cultural_knowledge_object"},
    {"category": "commonsense", "subcategory": "temporal_understanding"},
    {"category": "commonsense", "subcategory": "social_cultural_knowledge_scene"},

    {"category": "compositional", "subcategory": "creative_compositional"},
    {"category": "compositional", "subcategory": "inferential_spatial"},
    {"category": "compositional", "subcategory": "prescriptive_spatial"},

    {"category": "concept_mixing", "subcategory": "functional_mixing"},
    {"category": "concept_mixing", "subcategory": "literal_mixing"},

    {"category": "logical", "subcategory": "abductive"},
    {"category": "logical", "subcategory": "categorical"},
    {"category": "logical", "subcategory": "conjunctive"},
    {"category": "logical", "subcategory": "deductive"},
    {"category": "logical", "subcategory": "disjunctive"},
    {"category": "logical", "subcategory": "hypothetical"},
    {"category": "logical", "subcategory": "sufficient_conditional"},

    {"category": "numerical", "subcategory": "approximate_number_generation"},
    {"category": "numerical", "subcategory": "conceptual_quantitative"},
    {"category": "numerical", "subcategory": "exact_number_generation"},

    {"category": "mathematical", "subcategory": "combinatorial"},
    {"category": "mathematical", "subcategory": "cryptographic_encoding"},
    {"category": "mathematical", "subcategory": "geometrical_transformations"},
    {"category": "mathematical", "subcategory": "mathematical_function"},
    {"category": "mathematical", "subcategory": "number_theory"},
    {"category": "mathematical", "subcategory": "spatial_reasoning"},
    {"category": "mathematical", "subcategory": "vector_matrix_visualization"},
    {"category": "mathematical", "subcategory": "set_theory"},

    {"category": "causal", "subcategory": "cause_to_effect"},
    {"category": "causal", "subcategory": "effect_to_cause"},
]
PROMPT="""
# Text-to-Image Quality Evaluation Protocol 
# ## System Instruction 
You are an AI quality auditor for text-to-image generation. Answer these questions with ABSOLUTE RUTHLESSNESS. 
Only images meeting the HIGHEST standards should receive top scores.

## Task Overview
The image is prompt by the prompt: 
[PROMPT]

## Question List
[QUESTION LIST]

## Output Format
You can analyze in your output, but ensure the final line of your output is formatted as follows:

## Important Enforcement
- As long as the answer to the question of other confirmed valid permutation combinations has a score not equal to 1, the scores for the two questions of whether there are repeated permutations and whether there are invalid permutations will both be 0.

```json
{
    "id": score,
    ...
}
``` 
]
"""
def get_llm_response(prompt,image_path):     
    from openai import OpenAI
    import base64
    client = OpenAI(api_key= API_KEY)  

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    response = client.chat.completions.create(
        temperature=0.1,
        model="gpt-4o",  # Use the vision-preview model for image analysis
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )
    return(response.choices[0].message.content)