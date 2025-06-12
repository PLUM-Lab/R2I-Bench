sufficient_conditional = [
    {
        "Prompt": "If a person is present, then they are squatting. Generate an image of a library with many people.",
        "Reference Caption": "All people in the library are squatting; none are standing or sitting.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 1,
        "Assessment Point": "Since presence implies squatting, every visible person must be in a squatting posture; standing or sitting would contradict the sufficient conditional."
    },
    {
        "Prompt": "If a flower is present, then it is wilting. Generate an image of a vibrant garden full of flowers.",
        "Reference Caption": "All flowers have drooping petals, browned edges, or dried stems.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 2,
        "Assessment Point": "Given that flower presence implies wilting, every flower in the garden must exhibit signs of decay, not blooming or healthy appearance."
    },
    {
        "Prompt": "If a light is turned on, then it is red. Generate an image of a bird’s-eye view city street with many lights at night.",
        "Reference Caption": "All lights in the city street are red; no other colors are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 3,
        "Assessment Point": "Being turned on implies being red, so every light that is illuminated must be red to satisfy the logic of the condition."
    },
    {
        "Prompt": "If a pot is present, then it is boiling. Generate an image of a kitchen with many pots.",
        "Reference Caption": "All pots have visible steam, bubbles, or vigorous motion in their contents.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 4,
        "Assessment Point": "As pot presence implies boiling, every depicted pot must show boiling activity—steam or bubbling—regardless of whether it's in use or not."
    },
    {
        "Prompt": "If a bird is present, then it is a seagull. Generate an image of a beach with many birds.",
        "Reference Caption": "Only white/gray seabirds with long wings (no sparrows, pelicans, or parrots).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 5,
        "Assessment Point": "Bird presence requires the bird to be a seagull, so the image must contain no other bird types to uphold the sufficient conditional."
    },
    {
        "Prompt": "If a computer is turned on, then its screen is green. Generate an image of an office with lots of computers.",
        "Reference Caption": "All computers have green screens; no other screen colors are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 6,
        "Assessment Point": "Any computer that is powered on must have a green screen; the image meets this by restricting all visible screens to green."
    },
    {
        "Prompt": "If a cloud is present, then it is dark. Generate an image of a mountain landscape with many clouds.",
        "Reference Caption": "All clouds are deep gray or black (no white/fluffy cumulus clouds).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 7,
        "Assessment Point": "Presence of clouds implies darkness, so all clouds must appear ominous or stormy to satisfy the logical requirement."
    },
    {
        "Prompt": "If a student is present, then they are raising their hand. Generate an image of a classroom with many students.",
        "Reference Caption": "Every student has at least one arm raised (no sitting/standing with arms down).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 8,
        "Assessment Point": "Every depicted student must have a raised hand since being present entails that condition per the prompt’s logic."
    },
    {
        "Prompt": "If a plate is present, then it is empty. Generate an image of a busy restaurant with many dishes.",
        "Reference Caption": "All plates have no food (clean or with crumbs, but no intact dishes).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 9,
        "Assessment Point": "Plate presence implies emptiness, so all shown plates must have no food regardless of the dining context."
    },
    {
        "Prompt": "If a vehicle is moving, then it is a truck. Generate an image of a highway with many cars.",
        "Reference Caption": "All cars in motion are large trucks (stationary cars can be sedans or SUVs).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 10,
        "Assessment Point": "Only moving vehicles must be trucks—stationary ones are unrestricted—so all driving cars must appear as trucks to fulfill the condition."
    },
    {
        "Prompt": "If a tree is present, then it has no leaves. Generate an image of a dense forest.",
        "Reference Caption": "All trees are bare (no leaves), regardless of species or season.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 11,
        "Assessment Point": "Presence of a tree requires leaflessness; so even in a dense forest, all trees must appear bare to honor the sufficient condition."
    },
    {
        "Prompt": "If a person is walking, then they are holding an umbrella. Generate a busy city street with many pedestrians.",
        "Reference Caption": "All walking people have umbrellas.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 12,
        "Assessment Point": "Being in motion (walking) implies umbrella-holding; so every moving pedestrian must have an umbrella regardless of weather."
    },
    {
        "Prompt": "If a flower is present, then it is white. Generate a vibrant garden with many flowers.",
        "Reference Caption": "All flowers (roses, tulips, etc.) are exclusively white.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 13,
        "Assessment Point": "Flower presence requires whiteness; so the image must avoid any non-white flowers, despite the vibrant garden setting."
    },
    {
        "Prompt": "If a bird is on water, then it is a duck. Generate a lake with many birds.",
        "Reference Caption": "Only ducks float on water; other bird species may fly or perch on land.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 14,
        "Assessment Point": "Birds on water must be ducks; thus, any floating birds in the image must be depicted as ducks, while others can be elsewhere."
    },
    {
        "Prompt": "If a vehicle is moving, then it is a bicycle. Generate a city road with many cars.",
        "Reference Caption": "Moving bicycles dominate the scene; cars/buses are parked or stationary.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 15,
        "Assessment Point": "Motion implies bicycle; therefore, only bicycles can be shown in motion, while all other vehicles must be still."
    },
    {
        "Prompt": "If a window is open, then its curtains are drawn back. Generate a room with many windows.",
        "Reference Caption": "Open windows show pulled-aside curtains; closed windows may have closed curtains.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 16,
        "Assessment Point": "Open windows must have open curtains; so any window shown open must match this visual cue, but closed windows are unrestricted."
    },
    {
        "Prompt": "If a cat is black, then it wears a collar. Generate a mixed scene with colorful cats.",
        "Reference Caption": "All black cats are wearing collars; other cats may or may not have collars.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 17,
        "Assessment Point": "Black coloration entails having a collar; therefore, only black cats must have visible collars, others are optional."
    },
    {
        "Prompt": "If a fruit is in a bowl, then it is an apple. Generate a kitchen counter with a bowl filled with many fruits.",
        "Reference Caption": "The bowl contains only apples; other fruits (bananas, oranges) may sit outside it.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 18,
        "Assessment Point": "Being in a bowl implies being an apple; so all fruits shown inside the bowl must be apples to satisfy the logical relation."
    },
    {
        "Prompt": "If a cat is present, then it is wearing a bow tie. Generate an image of a living room with several cats.",
        "Reference Caption": "All cats in the image have bow ties.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 19,
        "Assessment Point": "Presence of any cat necessitates a bow tie; the scene ensures this by only displaying cats that wear bow ties."
    },
    {
        "Prompt": "If a car is parked, then it is blue. Generate an image of a busy parking lot.",
        "Reference Caption": "All parked cars are blue; moving cars may have other colors.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 20,
        "Assessment Point": "Parked status implies blue coloration; all stationary vehicles must therefore appear blue in the image."
    },
    {
        "Prompt": "If a bird is sitting on a branch, then it is a parrot. Generate an image of a tree with many birds.",
        "Reference Caption": "Only parrots are shown on branches; other birds may fly or stand on the ground.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 21,
        "Assessment Point": "Being on a branch implies being a parrot, so only parrots can be positioned on branches in the image."
    },
    {
        "Prompt": "If a tree is tall, then it has a swing. Generate an image of a park with trees.",
        "Reference Caption": "Swings appear only on tall trees; shorter trees lack them.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 22,
        "Assessment Point": "Tallness is a sufficient condition for having a swing, so only tall trees should show swings in the generated scene."
    },
    {
        "Prompt": "If a dog is running, then it has a leash. Generate an image of a dog park with many dogs.",
        "Reference Caption": "Running dogs have leashes; sitting or walking dogs may not.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 23,
        "Assessment Point": "Running implies leashed, so all dogs depicted in motion must visibly wear leashes."
    },
    {
        "Prompt": "If a window is open, then there is a curtain blowing outward. Generate an image of a house exterior with many windows visible.",
        "Reference Caption": "Open windows show flowing curtains; closed windows have still or no curtains.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 24,
        "Assessment Point": "Open windows must be paired with outward-blowing curtains to satisfy the conditional structure."
    },
    {
        "Prompt": "If a bicycle is moving, then it has a basket. Generate an image of a busy street with many bicycles.",
        "Reference Caption": "Moving bicycles have baskets; stationary ones may lack them.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 25,
        "Assessment Point": "Motion is sufficient for basket presence, so all bicycles in motion must visually carry baskets."
    },
    {
        "Prompt": "If a tree has flowers, then it has no leaves. Generate an image of a garden with various trees.",
        "Reference Caption": "Flowering trees are leafless; non-flowering trees may have leaves.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 26,
        "Assessment Point": "Floral presence dictates leaflessness; so any tree bearing flowers must appear entirely bare of leaves."
    },
    {
        "Prompt": "If a lamp is turned on, then it emits yellow light. Generate an image of a room with many lamps at night.",
        "Reference Caption": "All active lamps glow yellow; unlit lamps may be dark or another color.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 27,
        "Assessment Point": "Illumination implies yellow emission; thus, any lamp depicted as on must emit yellow light."
    },
    {
        "Prompt": "If a fish is in an aquarium, then it is orange. Generate an image of an aquarium with many fish.",
        "Reference Caption": "All fish inside the aquarium are orange; other fish (if present) may vary.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 28,
        "Assessment Point": "Aquarium location is sufficient for orange coloration, so all fish inside must be orange, regardless of type."
    },
    {
        "Prompt": "If a child is holding a balloon, then it is red. Generate an image of a birthday party with many children 拿着气球.",
        "Reference Caption": "All balloons in children’s hands are red; decorations or loose balloons can be any color.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 29,
        "Assessment Point": "Balloon-holding by children requires the balloon to be red, so only those held are constrained in color."
    },
    {
        "Prompt": "If it is raining, then all umbrellas are closed. Generate an image of a busy rainy city street.",
        "Reference Caption": "All umbrellas are closed; none are open despite the rain.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 30,
        "Assessment Point": "Rain implies closed umbrellas in this setting, so no open umbrellas can appear in the scene despite the weather."
    },
    {
        "Prompt": "If a tree is present, then its leaves are blue. Generate an image of a mountain landscape in autumn.",
        "Reference Caption": "All trees have blue leaves, with no autumn colors (e.g., red, yellow, or brown).",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 31,
        "Assessment Point": "Presence of a tree implies blue leaves, so all visible trees must reject natural autumn colors and have blue foliage."
    },
    {
        "Prompt": "If a person is swimming, then they are wearing a life jacket. Generate an image of a crowded beach.",
        "Reference Caption": "Every swimmer in the water or on the shore has a visible life jacket.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 32,
        "Assessment Point": "Swimming entails wearing a life jacket; hence, any person shown swimming must visibly have one on."
    },
    {
        "Prompt": "If a person is standing, then they are wearing green clothes. Generate a busy city street with pedestrians.",
        "Reference Caption": "All standing people are wearing green clothes; no one standing is wearing any other color.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 33,
        "Assessment Point": "Standing is sufficient for green attire, so every standing individual must be wearing green clothes."
    },
    {
        "Prompt": "If a book is closed, then it is under the bed. Generate a room with bookshelves and many books.",
        "Reference Caption": "Open books only appear on tables; closed books may be on shelves/chairs.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 34,
        "Assessment Point": "Being closed implies location under the bed; thus, closed books cannot be visible elsewhere unless under the bed."
    },
    {
        "Prompt": "If a car is moving, then it has tinted windows. Generate an image of a highway with many cars.",
        "Reference Caption": "All moving cars have tinted windows; stationary cars may have clear windows.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 35,
        "Assessment Point": "Motion necessitates tinted windows, so all cars in motion must visibly feature window tinting."
    },
    {
        "Prompt": "If a tree is large, then it has a bird’s nest. Generate an image of a forest with various trees.",
        "Reference Caption": "Large trees have visible bird’s nests; smaller trees do not.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 36,
        "Assessment Point": "Largeness of a tree ensures a bird’s nest, so all large trees must include one in the visual output."
    },
    {
        "Prompt": "If it is snowing, then all vehicles are black. Generate an image of a snow-covered street with many cars.",
        "Reference Caption": "All vehicles on the snow-covered street are black; no vehicles are of any other color.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 37,
        "Assessment Point": "Snowfall is sufficient to enforce black vehicle coloration, so no other vehicle color should be shown during snow."
    },
    {
        "Prompt": "If a child is standing, then they are wearing glasses. Generate an image of a playground with many children.",
        "Reference Caption": "All standing children are wearing glasses; sitting or lying children are not.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 38,
        "Assessment Point": "Standing implies glasses; hence, only standing children must wear them, regardless of others’ actions."
    },
    {
        "Prompt": "If a toothbrush is present, then it is in a cup. Generate an image of a bathroom with several cups.",
        "Reference Caption": "All toothbrushes are inside cups; no toothbrushes are lying on counters or sinks.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 39,
        "Assessment Point": "Presence of a toothbrush mandates cup placement, so no toothbrush may appear outside a cup."
    },
    {
        "Prompt": "If a towel is on a hook, then it is folded. Generate an image of a bathroom with many towels hanging.",
        "Reference Caption": "All towels on hooks are neatly folded; no towels are hanging loosely.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 40,
        "Assessment Point": "Being on a hook implies folded state, so no towel on a hook can appear unfolded or draped loosely."
    },
    {
        "Prompt": "If a spoon is in the kitchen, then it is inside a drawer. Generate an image of a kitchen with lots of spoons.",
        "Reference Caption": "All spoons are inside drawers; none are left on counters.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 41,
        "Assessment Point": "Being in the kitchen is sufficient for being in a drawer, so spoons must not appear on counters or elsewhere."
    },
    {
        "Prompt": "If a plate is on the dining table, then it is clean. Generate an image of a dining room with a table full of plates.",
        "Reference Caption": "All plates on the dining table are clean; no plates are dirty or stacked.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 42,
        "Assessment Point": "Plate presence on the table guarantees cleanliness, so no dirty or stacked plates can be visible on the table."
    },
    {
        "Prompt": "If a cup is in the living room, then it is to the right of the television. Generate an image of a living room with several cups.",
        "Reference Caption": "All cups are placed on tables; none are on the floor or shelves.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 43,
        "Assessment Point": "Cup presence in the living room implies placement to the right of the TV, so all cups must be situated accordingly in the image."
    },
    {
        "Prompt": "If a cell phone is on a table, then it is charging. Generate an image of a desk with many cell phones.",
        "Reference Caption": "All cell phones on tables are charging; none are turned off or unplugged.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 44,
        "Assessment Point": "Tabletop presence implies charging status, so each phone on the table must show signs of being charged (e.g., cable connected, screen on)."
    },
    {
        "Prompt": "If a knife is in the kitchen, then it is in a drawer. Generate an image of a kitchen with several drawers.",
        "Reference Caption": "All knives are in drawers; none are left on countertops.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 45,
        "Assessment Point": "Kitchen presence necessitates being stored in a drawer, so no knives can appear on counters or cutting boards."
    },
    {
        "Prompt": "If a chair is in the dining room, then it is placed around a table. Generate an image of a dining room with several chairs.",
        "Reference Caption": "All chairs are placed around the dining table; none are in corners or out of place.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 46,
        "Assessment Point": "Dining room location requires proper placement around a table, so scattered or misplaced chairs violate the condition."
    },
    {
        "Prompt": "If a pen is on a desk, then it is on top of a notebook. Generate an image of an office desk with pens and notebooks.",
        "Reference Caption": "All pens are next to a notebook; no pens are scattered alone.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 47,
        "Assessment Point": "Pen presence on the desk entails location atop a notebook, so all pens must visually align with notebooks, not stand alone."
    },
    {
        "Prompt": "If a broom is in the hallway, then it is hanging from the ceiling. Generate an image of a hallway with many brooms.",
        "Reference Caption": "The broom is hanging from the ceiling; it is not leaning against the wall or lying on the floor.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 48,
        "Assessment Point": "Hallway presence guarantees ceiling suspension, so brooms must not rest on walls or floors."
    },
    {
        "Prompt": "If a jacket is hanging on a hook, then it is green. Generate an image of a hallway with many jackets.",
        "Reference Caption": "All jackets hanging on hooks are green; no other colors are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 49,
        "Assessment Point": "Being hung on a hook implies a green color, so any jacket on a hook must appear green, regardless of style or type."
    },
    {
        "Prompt": "If a calendar is on the wall, then it is showing the month of April. Generate an image of a living room with many calendars on the wall.",
        "Reference Caption": "The calendar shows the month of April; no other months are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 50,
        "Assessment Point": "Presence on the wall implies it must be April, so every calendar must visibly display April only."
    },
    {
        "Prompt": "If a clock is on the wall, then it is showing 3 PM. Generate an image of a room with many clocks on the wall.",
        "Reference Caption": "The clock shows 3 PM; no other times are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 51,
        "Assessment Point": "Being a wall-mounted clock ensures the time shown is 3 PM; other times would contradict the conditional rule."
    },
    {
        "Prompt": "If a shoe is by the door, then it is a high heel. Generate an image of an entryway with many shoes by the door.",
        "Reference Caption": "All shoes by the door are high heels; no other types of shoes are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 52,
        "Assessment Point": "Shoes placed by the door must be high heels due to the conditional; showing sneakers or boots would break logical consistency."
    },
    {
        "Prompt": "If a pair of scissors is on the desk, then it is holding a piece of paper. Generate an image of a desk with many scissors and paper.",
        "Reference Caption": "The scissors are always holding a piece of paper; no scissors are left alone or with other objects.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 53,
        "Assessment Point": "The condition requires all scissors on the desk to hold paper, so all depicted scissors must visibly grip paper."
    },
    {
        "Prompt": "If a painting is on the wall, then it is a landscape. Generate an image of a living room with a variety of paintings on the walls.",
        "Reference Caption": "All paintings on the wall are landscapes; no abstract or portrait paintings are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 54,
        "Assessment Point": "Wall placement implies landscape subject matter; displaying portraits or abstracts would violate the prompt's rule."
    },
    {
        "Prompt": "If a syringe is in the hospital, then it is inside a sterilization container. Generate an image of a hospital with many syringes.",
        "Reference Caption": "All syringes are inside sterilization containers; none are left on the counters.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 55,
        "Assessment Point": "Being in the hospital implies being enclosed in sterilization containers, ensuring sterility as per the conditional logic."
    },
    {
        "Prompt": "If a blood pressure cuff is in the examination room, then it is on the floor. Generate an image of an examination room with many blood pressure cuffs.",
        "Reference Caption": "All blood pressure cuffs are on the floor; none are placed neatly on tables.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 56,
        "Assessment Point": "Examination room presence mandates floor location; table placement would contradict the conditional structure."
    },
    {
        "Prompt": "If a thermometer is in the hospital room, then it is under the bed. Generate an image of a hospital room with several thermometers.",
        "Reference Caption": "All thermometers are under the beds; none are left beside the patients.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 57,
        "Assessment Point": "Being in a hospital room implies the thermometer is under the bed, so visible thermometers must adhere to this spatial rule."
    },
    {
        "Prompt": "If a bandage is in the emergency room, then it is next to a first aid kit. Generate an image of an emergency room with several bandages.",
        "Reference Caption": "All bandages are next to first aid kits; none are scattered or misplaced around the room.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 58,
        "Assessment Point": "Emergency room presence requires proximity to first aid kits, so the placement of all bandages must reflect that relation."
    },
    {
        "Prompt": "If a stethoscope is in the clinic, then it is not hanging on a hook. Generate an image of a clinic with several stethoscopes.",
        "Reference Caption": "No stethoscopes are hanging on hooks; all stethoscopes are placed on tables or desks.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 59,
        "Assessment Point": "The condition forbids stethoscopes from hanging if they are in the clinic, so all must be placed elsewhere such as on tables or desks."
    },
    {
        "Prompt": "If a saw is present, then it is cutting wood. Generate an image of a workshop with a large number of saws",
        "Reference Caption": "All saws are actively cutting through wood, no saw is unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 60,
        "Assessment Point": "The conditional requires that the presence of a saw implies active cutting, so all depicted saws must be in operation on wood."
    },
    {
        "Prompt": "If a wrench is present, then it is being used. Generate an image of a mechanic workshop with many tools.",
        "Reference Caption": "All wrenches are in use, either in the hands of a mechanic or attached to a machine.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 61,
        "Assessment Point": "Presence implies usage per the condition, so every wrench must be shown as being handled or attached in active use."
    },
    {
        "Prompt": "If a screwdriver is present, then it is in use. Generate an image of a toolbox with many tools.",
        "Reference Caption": "All screwdrivers are actively turning screws; none are idle or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 62,
        "Assessment Point": "Any screwdriver in the image must be engaged in activity (e.g., turning screws) to satisfy the stated conditional logic."
    },
    {
        "Prompt": "If a hammer is present, then it is hitting a nail. Generate an image of a construction site with lots of hammers.",
        "Reference Caption": "All hammers are striking nails; no hammer is idle.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 63,
        "Assessment Point": "The presence of a hammer necessitates it being shown mid-strike or making contact with nails to reflect the condition."
    },
    {
        "Prompt": "If a drill is present, then it is drilling a hole. Generate an image of a garage with lots of drills.",
        "Reference Caption": "All drills are drilling into surfaces like wood, metal, or plastic.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 64,
        "Assessment Point": "The logic demands active use; each drill shown must be visibly boring holes to fulfill the ‘if present, then drilling’ condition."
    },
    {
        "Prompt": "If a paintbrush is present, then it is not covered in paint. Generate an image of a painter’s studio with unfinished projects.",
        "Reference Caption": "All paintbrushes have no visible paint on them.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 65,
        "Assessment Point": "Presence of a paintbrush implies it must be clean; painted brushes would violate the conditional rule stated in the prompt."
    },
    {
        "Prompt": "If a ruler is present, then it is measuring length. Generate an image of an architect’s workspace with many rulers.",
        "Reference Caption": "All rulers are laid out flat and in use for precise measurements.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 66,
        "Assessment Point": "Each ruler must be shown as actively aligned or used for measurement to meet the sufficient conditional requirement."
    },
    {
        "Prompt": "If a tape is present, then it is sealing something. Generate an image of an office with many tapes.",
        "Reference Caption": "All tapes are sealing boxes, packages, or other containers.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 67,
        "Assessment Point": "The condition states that the presence of tape implies it is actively sealing; thus, every tape in the scene must be shown in use sealing an object."
    },
    {
        "Prompt": "If a chain is present, then it is attached to something. Generate an image of a warehouse with a large number of chains.",
        "Reference Caption": "All chains are attached to machines, hooks, or other items.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 68,
        "Assessment Point": "To fulfill the conditional, each chain must be visually connected to an object, showing it is not loose or free-standing."
    },
    {
        "Prompt": "If a butterfly is present, then it is resting on a leaf. Generate an image of a garden with many insects.",
        "Reference Caption": "All butterflies are resting on leaves; none are flying or perched elsewhere.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 69,
        "Assessment Point": "The rule requires all butterflies to be shown only in the specific context of resting on leaves, excluding flying or other postures."
    },
    {
        "Prompt": "If a rabbit is present, then it is eating a carrot. Generate an image of a meadow with many animals.",
        "Reference Caption": "All rabbits are holding or nibbling carrots.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 70,
        "Assessment Point": "The conditional mandates that any rabbit must be shown eating; thus, all rabbits must be interacting with carrots to satisfy the rule."
    },
    {
        "Prompt": "If a squirrel is present, then it is standing under a tree. Generate an image of a forest with many squirrels.",
        "Reference Caption": "All squirrels are standing under trees; none are climbing or sitting elsewhere.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 71,
        "Assessment Point": "Squirrel presence must correlate with location under a tree; any squirrels in the image must be shown specifically in that setting."
    },
    {
        "Prompt": "If a spider is present, then it has no web. Generate an image of a forest with many spiders.",
        "Reference Caption": "All spiders are present without webs; none are weaving or have webs around them.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 72,
        "Assessment Point": "The condition negates web presence when a spider is present, so all spiders must appear isolated without any visible webs."
    },
    {
        "Prompt": "If a turtle is present, then it is retracted into its shell. Generate an image of a beach with many turtles.",
        "Reference Caption": "All turtles are retracted into their shells; none are fully extended.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 73,
        "Assessment Point": "Presence of a turtle must visually coincide with shell retraction to align with the logic stated in the prompt."
    },
    {
        "Prompt": "If a hair tie is present, then it is tied in hair. Generate an image of many hair ties.",
        "Reference Caption": "All hair ties are tied in hair; none are left lying loose or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 74,
        "Assessment Point": "The rule binds presence with being in use; hence, each hair tie must be visibly worn and not just scattered or idle."
    },
    {
        "Prompt": "If a sock is present, then it is worn on the hand. Generate an image of many socks.",
        "Reference Caption": "All socks are worn on hands; none are on feet or lying around.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 75,
        "Assessment Point": "The prompt establishes a conditional rule where any present sock must be on a hand. The caption satisfies this by showing no socks on feet or unused."
    },
    {
        "Prompt": "If a necklace is present, then it is worn on the ankle. Generate an image of many necklaces.",
        "Reference Caption": "All necklaces are worn on ankles; none are worn around necks or left unworn.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 76,
        "Assessment Point": "The conditional mandates that every necklace must be on an ankle if present. The caption conforms by placing all necklaces on ankles."
    },
    {
        "Prompt": "If a person is present, then they are squatting in a horse stance. Generate an image of a hospital with many people.",
        "Reference Caption": "All people are squatting in a horse stance; none are standing or sitting.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 77,
        "Assessment Point": "The logic requires all people in the image to be squatting in horse stance. The caption ensures this condition is met for every individual shown."
    },
    {
        "Prompt": "If food is present, then it is placed in a bucket. Generate an image of a kitchen with lots of food.",
        "Reference Caption": "All food is placed in buckets; none are on countertops or tables.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 78,
        "Assessment Point": "Any food depicted must be in a bucket according to the prompt. The caption guarantees this by excluding food from other locations."
    },
    {
        "Prompt": "If an eggplant is present, then it is cut into pieces. Generate an image of a garden with many eggplants.",
        "Reference Caption": "All eggplants are cut into pieces; none are left whole.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 79,
        "Assessment Point": "The sufficient condition requires all visible eggplants to be sliced. The caption reflects this exactly by showing no whole eggplants."
    },
    {
        "Prompt": "If a dragon fruit is present, then it is squashed. Generate an image of a bowl with many foods.",
        "Reference Caption": "All dragon fruits are squashed; none are whole or intact.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 80,
        "Assessment Point": "The logical rule demands that all dragon fruits must appear squashed. The caption complies fully with this requirement."
    },
    {
        "Prompt": "If a hairpin is present, then it is worn on the head. Generate an image of many hairpins.",
        "Reference Caption": "All hairpins are worn on the head; none are lying around or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 81,
        "Assessment Point": "Given the rule, any visible hairpin must be on someone’s head. The caption correctly ensures there are no loose or unused hairpins."
    },
    {
        "Prompt": "If a ring is present, then it is worn on the toe. Generate an image of many rings.",
        "Reference Caption": "All rings are worn on toes; none are worn on fingers or lying around.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 82,
        "Assessment Point": "The condition states that every ring must be on a toe. The caption follows this strictly by avoiding finger-worn or loose rings."
    },
    {
        "Prompt": "If a macadamia nut is present, then its flesh is eaten. Generate an image of many sunflower seeds.",
        "Reference Caption": "All macadamia nuts have their flesh eaten; no nuts are left whole.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 83,
        "Assessment Point": "According to the logic, any macadamia nut shown must be consumed. The caption upholds this by showing no intact nuts."
    },
    {
        "Prompt": "If a nail polish is present, then it is used up. Generate an image of many nail polishes.",
        "Reference Caption": "All nail polishes are used up; none are full or untouched.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 84,
        "Assessment Point": "The prompt requires that any visible nail polish bottle must be empty. The caption aligns by excluding full or new bottles."
    },
    {
        "Prompt": "If a cabbage is present, then it is cooked into a dish. Generate an image of a garden with many cabbages.",
        "Reference Caption": "All cabbages are cooked into dishes; none are left raw or in the garden.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 85,
        "Assessment Point": "The conditional states that any cabbage must be cooked. The caption fulfills this by showing no raw or garden cabbages."
    },
    {
        "Prompt": "If a backpack is present, then it is hung on a hook. Generate an image of a dance studio with many backpacks.",
        "Reference Caption": "All backpacks are hung on hooks; none are left on the floor or scattered around.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 86,
        "Assessment Point": "The logic requires all backpacks to be on hooks if present. The caption complies by excluding misplaced backpacks."
    },
    {
        "Prompt": "If a stone is present, then it is green. Generate an image of a stone market with many stones.",
        "Reference Caption": "All stones are green; no other colors are visible.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 87,
        "Assessment Point": "The conditional demands that all visible stones be green. The caption aligns by eliminating any stones of other colors."
    },
    {
        "Prompt": "If a fish is present, then it is cooked into a dish. Generate an image of a kitchen with many fish.",
        "Reference Caption": "All fish are cooked into dishes; none are left raw or uncooked.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 88,
        "Assessment Point": "The rule states any present fish must be cooked. The caption enforces this by avoiding raw or unprepared fish."
    },
    {
        "Prompt": "If a piece of leather is present, then it is completely made into a bag. Generate an image of a leather workshop with many pieces of leather.",
        "Reference Caption": "All pieces of leather are made into bags; none are left as raw hides or unprocessed.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 89,
        "Assessment Point": "The prompt condition requires all leather to become bags. The caption adheres by excluding any unfinished material."
    },
    {
        "Prompt": "If wool is present, then it is completely spun into yarn. Generate an image of a spinning workshop with many wool fibers.",
        "Reference Caption": "All wool fibers are spun into yarn; none are left unspun or in their raw form.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 90,
        "Assessment Point": "The rule states all wool should be spun into yarn. The caption aligns by showing no raw fibers remain."
    },
    {
        "Prompt": "If a piece of copper is present, then it is completely made into a wire. Generate an image of a copper factory with many copper pieces.",
        "Reference Caption": "All pieces of copper are made into wires; none are left as raw chunks or ingots.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 91,
        "Assessment Point": "The prompt demands that all copper be formed into wire. The caption fulfills this by showing no copper in its original form."
    },
    {
        "Prompt": "If a coconut is present, then it is cracked open and eaten. Generate an image of a tropical market with many coconuts.",
        "Reference Caption": "All coconuts are cracked open and eaten; none are left whole or uncracked.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 92,
        "Assessment Point": "The conditional states that all coconuts must be consumed. The caption satisfies this by excluding whole coconuts."
    },
    {
        "Prompt": "If a test tube is present, then it is filled with solid. Generate an image of a laboratory bench with many test tubes.",
        "Reference Caption": "All test tubes are filled with solids; none are empty or filled with liquids.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 93,
        "Assessment Point": "The prompt specifies solids inside any present test tube. The caption ensures conformity by avoiding liquid or empty tubes."
    },
    {
        "Prompt": "If a glass slide is present, then it is being used for microscopy. Generate an image of a laboratory with many glass slides.",
        "Reference Caption": "All glass slides are being used for microscopy; none are left unused or unprepared.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 94,
        "Assessment Point": "The conditional requires all present glass slides to be in use for microscopy, which is satisfied by the caption excluding unused or idle slides."
    },
    {
        "Prompt": "If a petri dish is present, then it contains a growing culture. Generate an image of a laboratory with many petri dishes.",
        "Reference Caption": "All petri dishes contain a growing culture; none are empty or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 95,
        "Assessment Point": "The rule implies that any petri dish must contain a culture. The caption conforms by avoiding depictions of empty or clean dishes."
    },
    {
        "Prompt": "If a lab coat is present, then it is being worn by a researcher. Generate an image of a laboratory with many lab coats.",
        "Reference Caption": "All lab coats are being worn by researchers; none are hanging or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 96,
        "Assessment Point": "The logic demands that all lab coats must be worn if present. The caption upholds this by not showing idle or hanging lab coats."
    },
    {
        "Prompt": "If a stir bar is present, then it is used for stirring a solution. Generate an image of a laboratory with many stir bars.",
        "Reference Caption": "All stir bars are in use for stirring solutions; none are unused or still.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 97,
        "Assessment Point": "Since the condition is that all stir bars are in active use, the caption confirms this by avoiding passive or idle stir bars."
    },
    {
        "Prompt": "If a mistletoe decoration is present, then it is hanging from the ceiling. Generate an image of a hallway with many mistletoe decorations.",
        "Reference Caption": "All mistletoe decorations are hanging from the ceiling; none are placed on the floor or walls.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 98,
        "Assessment Point": "The conditional requires ceiling placement of any mistletoe. The caption enforces this by excluding all other locations."
    },
    {
        "Prompt": "If a teddy bear is present, then it is hugged by a child. Generate an image of a room with many teddy bears.",
        "Reference Caption": "All teddy bears are being hugged by children; none are left alone or unused.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 99,
        "Assessment Point": "The rule says that any teddy bear must be hugged. The caption meets this by showing all bears in the arms of children."
    },
    {
        "Prompt": "If a model airplane is present, then it is placed on the bench. Generate an image of a park with many model airplanes.",
        "Reference Caption": "All model airplanes are placed on benches; none are on the ground or in the air.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 100,
        "Assessment Point": "The conditional links all airplanes to bench placement. The caption satisfies this by omitting any other location."
    },
    {
        "Prompt": "If a spinning top is present, then it is spinning. Generate an image of a table with many spinning tops.",
        "Reference Caption": "All spinning tops are spinning; none are stationary or untouched.",
        "Category": "logical",
        "Subcategory": "Sufficient Conditional",
        "id": 101,
        "Assessment Point": "The prompt demands that any spinning top must be in motion. The caption supports this by showing no idle tops."
    }
]
