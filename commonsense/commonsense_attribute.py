attribute = [
    {
        "Prompt": "A transparent water tank with a tennis ball and an iron block.",
        "Reference Caption": "The model should generate an image where the tennis ball is floating on the surface of the water, and the iron block is sunk to the bottom of the tank. The image should clearly differentiate between the two objects' positions in water, showing one buoyant and one submerged",
        "Assessment Point": "The tennis ball is less dense than water, so it floats on the surface, while the iron block, being denser than water, sinks to the bottom. This is based on the fundamental principle of buoyancy.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 1
    },
    {
        "Prompt": "A balloon filled with air in a room.",
        "Reference Caption": "The model should generate an image showing a balloon filled with air resting on the floor or suspended slightly, indicating its lack of significant buoyancy",
        "Assessment Point": "A balloon filled with air is less buoyant compared to one filled with lighter gases like helium, so it typically doesn't float or rise significantly, leading to it resting on the floor or suspended slightly in the air.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 2
    },
    {
        "Prompt": "An image of a seesaw with a child on one side and an adult on the other.",
        "Reference Caption": "The model should generate an image where the seesaw is significantly tilted due to the weight difference between the child and the adult. The elephant should be on the lower side, close to the ground, and the child should be on the higher side, elevated in the air. The seesaw should not be level",
        "Assessment Point": "The adult has more weight than the child, which causes the seesaw to tilt. The heavier side, with the adult, goes lower while the lighter side, with the child, rises higher. This is a basic principle of balance and weight distribution.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 3
    },
    {
        "Prompt": "A pair of scissors is cutting paper.",
        "Reference Caption": "The blades are aligned horizontally, with one blade above the paper and one below.",
        "Assessment Point": "Scissors work through opposing shear forces.  Vertical blade alignment or mismatched positioning would make cutting impossible.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 4
    },
    {
        "Prompt": "A used tea bag next to a cup.",
        "Reference Caption": "Damp, stained, and expanded tea bag.",
        "Assessment Point": "Used tea bags absorb water.  Incorrect: dry, pristine tea bag.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 5
    },
    {
        "Prompt": "A spoon in a glass of water.",
        "Reference Caption": "The spoon appears bent at the water’s surface due to refraction.",
        "Assessment Point": "If the model ignores light refraction, the spoon would render straight.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 6
    },
    {
        "Prompt": "A polar bear in summer.",
        "Reference Caption": "Yellow-tinged fur (not pure white).",
        "Assessment Point": "Polar bear fur becomes yellowish due to oxidation and oils in warmer months.  Pure white would indicate Arctic winter context.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 7
    },
    {
        "Prompt": "A smartphone charging wirelessly.",
        "Reference Caption": "Phone placed horizontally on a charging pad, no cables.",
        "Assessment Point": "Wireless charging requires specific positioning.  Failure might show a plugged-in cable.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 8
    },
    {
        "Prompt": "A mirror reflecting a red ball.",
        "Reference Caption": "A perfect red replica of the ball in the reflection.",
        "Assessment Point": "Incorrect color or distortion in the reflection would reveal ignorance of mirror properties (color fidelity and flatness).",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 9
    },
    {
        "Prompt": "A dog that just heard a loud noise.",
        "Reference Caption": "The dog’s ears are perked up, body tense, and tail lowered.",
        "Assessment Point": "Without knowledge of animal behavior, the model might show a relaxed dog, missing signs of alertness.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 10
    },
    {
        "Prompt": "A kangaroo sitting.",
        "Reference Caption": "The kangaroo uses its tail as a tripod for balance.",
        "Assessment Point": "If the model doesn’t know kangaroos rely on their tails while sitting, it might depict the tail lifted or inactive.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 11
    },
    {
        "Prompt": "A pangolin in primary defensive behavior.",
        "Reference Caption": "The model should generate an image of a pangolin exhibiting its primary defensive behavior: curling into a tight ball. The scales should be prominently displayed, forming a protective armor around the animal. The head and limbs should be tucked inside the ball.",
        "Assessment Point": "Pangolins use their primary defensive behavior of curling into a tight ball to protect themselves from predators. This behavior is accompanied by the display of their tough, overlapping scales, which form an armor. The head and limbs are hidden inside to shield them from danger, which is why the Reference Caption image emphasizes these features.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 12
    },
    {
        "Prompt": "A bathroom mirror after a hot shower.",
        "Reference Caption": "Fogged/condensed mirror surface.",
        "Assessment Point": "Steam condenses on cool surfaces. Incorrect outputs might show a clear mirror, failing to infer this cause-effect relationship.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 13
    },
    {
        "Prompt": "A pair of glasses lying on a newspaper.",
        "Reference Caption": "The newspaper text is clearly visible through the lenses, slightly magnified or refracted.",
        "Assessment Point": "The model must correctly infer the refractive properties of lenses, rather than generating an opaque or incorrectly transparent lens.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 14
    },
    {
        "Prompt": "A sunflower outdoors at night.",
        "Reference Caption": "The sunflower’s head is slightly drooped or oriented downward.",
        "Assessment Point": "The model must understand sunflowers naturally lower their heads in the absence of sunlight, rather than facing upward or toward the nonexistent sun.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 15
    },
    {
        "Prompt": "A cat's eyes in bright sunlight.",
        "Reference Caption": "Cat’s pupils are vertical slits.",
        "Assessment Point": "Cat pupils contract to slits in bright light. Incorrect images would show round pupils, failing to apply biological knowledge.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 16
    },
    {
        "Prompt": "A person blowing on a dandelion clock.",
        "Reference Caption": "White seed tufts dispersing in the air.",
        "Assessment Point": "Models unaware that blowing scatters dandelion seeds might show intact seed heads.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 17
    },
    {
        "Prompt": "A popped popcorn kernel next to unpopped ones.",
        "Reference Caption": "The popped kernel is fluffy and white, contrasting with smooth, yellow unpopped kernels.",
        "Assessment Point": "Requires understanding heat-induced expansion. Failure might show uniform kernels.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 18
    },
    {
        "Prompt": "A helium balloon in a braking car.",
        "Reference Caption": "Balloon floats toward the front windshield.",
        "Assessment Point": "Due to air density differences, lighter helium moves opposite to inertia.  A model lacking physics knowledge might show the balloon staying centered.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 19
    },
    {
        "Prompt": "A porcupine curled up to sleep.",
        "Reference Caption": "Quills lie flat against its body.",
        "Assessment Point": "Porcupines relax their quills when resting.  Models lacking zoological knowledge might depict raised, defensive quills.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 20
    },
    {
        "Prompt": "A flamingo resting in shallow water.",
        "Reference Caption": "The flamingo stands on one leg.",
        "Assessment Point": "Flamingos sleep/rest by tucking one leg close to their body. Models unaware of this behavior might depict two legs planted in water.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 21
    },
    {
        "Prompt": "A bat sleeping.",
        "Reference Caption": "The bat hangs upside down from a surface (e.g., a cave ceiling or tree branch).",
        "Assessment Point": "Bats sleep inverted.  A model lacking this knowledge might show a bat resting upright, akin to a bird.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 22
    },
    {
        "Prompt": "A squirrel storing acorns.",
        "Reference Caption": "Acorns buried underground or tucked into a tree hollow.",
        "Assessment Point": "An incorrect image might show acorns scattered randomly, ignoring squirrels’ food-hoarding behavior.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 23
    },
    {
        "Prompt": "A dog chasing its tail.",
        "Reference Caption": "The dog’s body twisted in a circular motion, attempting to bite its tail.",
        "Assessment Point": "An incorrect image might show a static dog near its tail, missing the dynamic action.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 24
    },
    {
        "Prompt": "An almost burnt out candle.",
        "Reference Caption": "The candle has melted down to a very short length, with the wax dripping down the sides.",
        "Assessment Point": "When a candle is nearly burnt out, it has typically melted to a very small size, and the remaining wax tends to drip down the sides due to the heat.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 25
    },
    {
        "Prompt": "A leftover used soap bar.",
        "Reference Caption": "The soap bar is thin.",
        "Assessment Point": "After repeated use, a soap bar naturally becomes thinner as it dissolves with each wash, leaving behind a smaller, thinner piece.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 26
    },
    {
        "Prompt": "A seesaw with uneven weights on both sides.",
        "Reference Caption": "One end of the seesaw is tilted.",
        "Assessment Point": "If the weights on both sides of the seesaw are uneven, the heavier side will cause the seesaw to tilt, as the balance is disrupted.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 27
    },
    {
        "Prompt": "A vintage clock showing 3 AM.",
        "Reference Caption": "The hour hand points towards the right. The minute hand points upwards.",
        "Assessment Point": "At 3 AM, the hour hand points towards the right (towards the 3 o'clock position), and the minute hand, marking the top of the hour, points upwards (towards the 12 o'clock position).",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 28
    },
    {
        "Prompt": "A stainless steel pan previously overheated.",
        "Reference Caption": "The pan has rainbow-like discoloration.",
        "Assessment Point": "When a stainless steel pan is overheated, the metal undergoes oxidation, which can result in a rainbow-like discoloration caused by light interference on the surface.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 29
    },
    {
        "Prompt": "A peacock sleeping.",
        "Reference Caption": "A peacock has its feathers closed.",
        "Assessment Point": "When a peacock sleeps, it typically folds its feathers close to its body to rest. This is a common behavior for many birds during sleep to protect their feathers and conserve body heat.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 30
    },
    {
        "Prompt": "A vintage clock showing noon",
        "Reference Caption": "Both the hour hand and the minute hand point straight up.",
        "Assessment Point": "At noon, the time is exactly 12:00, and in a typical analog clock, both the hour hand and minute hand point at the 12 o'clock position, which is straight up.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 31
    },
    {
        "Prompt": "An electric car parked at a charging station but not charging yet",
        "Reference Caption": "No cable is connecting the car to the charging infrastructure.",
        "Assessment Point": "If the car is parked at a charging station but not charging, the cable is not connected to the car, as the charging process hasn't started yet.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 32
    },
    {
        "Prompt": "An empty pan heated for a long time",
        "Reference Caption": "Smoke is rising from the pan.",
        "Assessment Point": "When a pan is heated for a long period without any food or liquid inside, the metal can reach a high temperature, causing any leftover residues or oils to burn and produce smoke.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 33
    },
    {
        "Prompt": "A sundae untouched for several hours",
        "Reference Caption": "The ice cream within the glass has melted into liquid form.",
        "Assessment Point": "If a sundae is left untouched for several hours, the ice cream will naturally melt due to heat and time, transitioning from solid to liquid form.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 34
    },
    {
        "Prompt": "A candle just blown out",
        "Reference Caption": "Smoke is seen rising from the candle's wick. No flame is burning at the candle's wick.",
        "Assessment Point": "When a candle is blown out, the flame is extinguished, but the heat from the wick causes the wax to release smoke, which rises from the wick. Without the flame, there is no longer a visible burning fire.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 35
    },
    {
        "Prompt": "An hourglass just finishing its counting",
        "Reference Caption": "The sand is mostly in the bottom half of the hourglass.",
        "Assessment Point": "When the hourglass finishes its counting, the sand has already fallen through the narrow passage, and most of it settles in the bottom half. The top half has little or no sand left.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 36
    },
    {
        "Prompt": "An hourglass just starting to count",
        "Reference Caption": "The sand is mostly in the upper half of the hourglass.",
        "Assessment Point": "At the start of the hourglass's timing, the sand is still in the top half and begins to flow down. Since the sand has just started, the upper half will still contain most of the sand.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 37
    },
    {
        "Prompt": "A lightbulb with a good circuit",
        "Reference Caption": "The bulb is lit.",
        "Assessment Point": "A good circuit means the electrical current flows properly through the lightbulb, causing it to light up. Without any disruption in the circuit, the bulb will be lit.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 38
    },
    {
        "Prompt": "Iron nails and a magnet",
        "Reference Caption": "The iron nails are attracted to the magnet.",
        "Assessment Point": "Iron is a magnetic material, so when placed near a magnet, it will be attracted to the magnet due to the magnetic force.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 39
    },
    {
        "Prompt": "A pen placed in a cup of water",
        "Reference Caption": "The submerged part of the pen appears bent.",
        "Assessment Point": "The pen is partly submerged in water, and due to the change in the speed of light as it passes through different mediums (air and water), refraction causes the submerged part to appear bent.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 40
    },
    {
        "Prompt": "A glass of water held upside-down",
        "Reference Caption": "Water spills onto the ground.",
        "Assessment Point": "When the glass is turned upside down, gravity causes the water to fall out due to the lack of support underneath the glass.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 41
    },
    {
        "Prompt": "A basketball in water",
        "Reference Caption": "The basketball is floating on the water's surface.",
        "Assessment Point": "A basketball is less dense than water, which allows it to float on the surface due to the principle of buoyancy.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 42
    },
    {
        "Prompt": "An open fridge disconnected from electricity",
        "Reference Caption": "The open fridge is not lighting up.",
        "Assessment Point": "When the fridge is disconnected from electricity, it no longer has the power to light up the interior, as the light inside requires electrical current to function.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 43
    },
    {
        "Prompt": "An iron ball in water",
        "Reference Caption": "The iron ball is sinking in the water.",
        "Assessment Point": "Iron is denser than water, which causes the iron ball to sink due to the force of gravity overpowering the buoyant force exerted by the water.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 44
    },
    {
        "Prompt": "A lightbulb with a broken circuit",
        "Reference Caption": "The bulb is unlit.",
        "Assessment Point": "A broken circuit means the electrical current cannot flow through the bulb, preventing it from lighting up.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 45
    },
    {
        "Prompt": "An empty bottle in water",
        "Reference Caption": "The empty bottle is floating on the water surface.",
        "Assessment Point": "An empty bottle displaces water, and since the bottle is less dense than the water, it floats rather than sinking.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 46
    },
    {
        "Prompt": "An eagle catching a fish",
        "Reference Caption": "The eagle is grasping or trying to grasp a fish with its claws. The eagle is spreading its wings above water.",
        "Assessment Point": "Eagles catch fish with their claws, and they typically spread their wings for stability while hovering or flying over water.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 47
    },
    {
        "Prompt": "A pot of salted water heated to 100 degrees Celsius",
        "Reference Caption": "The pot is not boiling.",
        "Assessment Point": "Boiling point for salted water is higher than 100 degrees Celsius, so it has not reached boiling yet at this temperature.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 48
    },
    {
        "Prompt": "A small bag of party balloons for sale",
        "Reference Caption": "The balloons are flat.",
        "Assessment Point": "Balloons for sale are often deflated to save space and ensure they can be inflated by the buyer.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 49
    },
    {
        "Prompt": "An eagle eating a fish",
        "Reference Caption": "The eagle has folded wings. The eagle is eating fish.",
        "Assessment Point": "An eagle in the act of eating a fish is often depicted with its wings folded to help with balance and focus on its prey. The Reference Caption description aligns with the visual of the eagle being engaged in the act of eating.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 50
    },
    {
        "Prompt": "A faucet that's turned off",
        "Reference Caption": "There is no water coming out of the faucet.",
        "Assessment Point": "When a faucet is turned off, the water flow is stopped. The commonsense reasoning is that no water would come out of the faucet when it's in the off position.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 51
    },
    {
        "Prompt": "A person igniting a wet match",
        "Reference Caption": "The match is not burning.",
        "Assessment Point": "A wet match would fail to catch fire because the moisture prevents it from lighting. This is a clear commonsense reasoning that a match needs to be dry to burn.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 52
    },
    {
        "Prompt": "A full bottle in water",
        "Reference Caption": "The full bottle is sinking in the water.",
        "Assessment Point": "A full bottle, being heavy and filled with liquid, would likely sink when placed in water. This is based on the concept that a higher density object typically sinks in water.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 53
    },
    {
        "Prompt": "A pot of water heated to 100 degrees celsius",
        "Reference Caption": "The pot is boiling.",
        "Assessment Point": "Water boils at 100°C at standard atmospheric pressure, so when water reaches this temperature, it will undergo the boiling process. This is a direct result of the physical property of water's boiling point.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 54
    },
    {
        "Prompt": "A squirrel hiding a nut",
        "Reference Caption": "A squirrel is burying a nut into the ground.",
        "Assessment Point": "Squirrels typically hide nuts by burying them in the ground to store food for later. This action is commonly associated with the act of hiding a nut.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 55
    },
    {
        "Prompt": "Newly hatched eggs",
        "Reference Caption": "Egg shells are cracking open and chickens are walking out.",
        "Assessment Point": "When eggs hatch, the shells crack open, and the chicks emerge from within. This is the natural process of new chicks being born.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 56
    },
    {
        "Prompt": "Cement mixed with water",
        "Reference Caption": "There is a sticky mixture of smooth, wet cement.",
        "Assessment Point": "When cement is mixed with water, it becomes a wet and sticky substance. This is the characteristic of cement once it is properly hydrated for use.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 57
    },
    {
        "Prompt": "A brick hit with a sledgehammer",
        "Reference Caption": "There is a pile of shattered brick debris.",
        "Assessment Point": "When a brick is hit forcefully with a sledgehammer, it will break into pieces, creating debris. This outcome is the natural result of a brick being struck with a heavy tool.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 58
    },
    {
        "Prompt": "A pebble in the water",
        "Reference Caption": "The pebble is submerged in water.",
        "Assessment Point": "A pebble, being small and dense, will sink and be submerged when placed in water. This is the typical behavior of a pebble in water.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 59
    },
    {
        "Prompt": "A mirror in a room without light",
        "Reference Caption": "A barely visible room is reflected.",
        "Assessment Point": "Without light, the mirror cannot reflect clearly, so the reflection will be dim and faint, making the room appear barely visible.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 60
    },
    {
        "Prompt": "A burning matchstick dipped into water",
        "Reference Caption": "The matchstick is nearly extinguished with a blackened tip.",
        "Assessment Point": "Dipping the matchstick into water will reduce its temperature and extinguish the flame, leaving the matchstick's tip blackened from the burn.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 61
    },
    {
        "Prompt": "Bats during the day",
        "Reference Caption": "Bats are hanging upside down and inside a house or a cave.",
        "Assessment Point": "Bats are nocturnal animals, so during the day they typically seek shelter in dark, quiet places like caves or buildings, where they hang upside down to rest.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 62
    },
    {
        "Prompt": "A punctured party balloon",
        "Reference Caption": "The balloon is wrinkled and flat.",
        "Assessment Point": "When a balloon is punctured, air escapes, causing it to deflate and wrinkle as it loses its shape.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 63
    },
    {
        "Prompt": "A butterfly on a rainy day",
        "Reference Caption": "A butterfly is hiding under a shelter.",
        "Assessment Point": "Butterflies are delicate and vulnerable to rain, so they typically seek shelter under leaves, trees, or other coverings to stay dry.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 64
    },
    {
        "Prompt": "A budding dandelion",
        "Reference Caption": "A yellow flower is about to blossom.",
        "Assessment Point": "A budding dandelion refers to the early stages of the dandelion flower's growth, which is typically yellow when it blooms.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 65
    },
    {
        "Prompt": "Hungry baby birds",
        "Reference Caption": "Baby birds have their mouths open.",
        "Assessment Point": "When baby birds are hungry, they instinctively open their mouths to be fed by their parents.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 66
    },
    {
        "Prompt": "A bedroom at night with no electricity",
        "Reference Caption": "The room is completely dark.",
        "Assessment Point": "Without electricity, the room would lack any source of light, causing it to be dark at night.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 67
    },
    {
        "Prompt": "A piece of paper in water",
        "Reference Caption": "The paper is completely wet and soaked.",
        "Assessment Point": "When a piece of paper is placed in water, it absorbs the liquid, resulting in it being wet and soaked.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 68
    },
    {
        "Prompt": "An oak tree in winter",
        "Reference Caption": "The tree has bare branches with no leaves.",
        "Assessment Point": "In winter, most deciduous trees, including oak trees, shed their leaves, leaving only bare branches.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 69
    },
    {
        "Prompt": "An egg dropped on the floor",
        "Reference Caption": "The egg is broken with yolk and white spilled out.",
        "Assessment Point": "When an egg is dropped, it is highly likely to break due to its fragile shell. The impact with the floor causes the egg to crack, spilling its contents, including the yolk and white.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 70
    },
    {
        "Prompt": "A penguin sliding on ice",
        "Reference Caption": "A penguin is sliding on its belly.",
        "Assessment Point": "Penguins are known to slide on their bellies as a means of locomotion on ice, utilizing their body shape and smooth surface to move efficiently on slippery ice.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 71
    },
    {
        "Prompt": "A glass of water dropped on the floor",
        "Reference Caption": "Water and a shattered glass are on the floor.",
        "Assessment Point": "When a glass containing water is dropped, the glass is likely to shatter upon impact with the floor. The water will spill out due to gravity and the glass being broken.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 72
    },
    {
        "Prompt": "A book left open in the rain",
        "Reference Caption": "The open book has wet and soaked pages.",
        "Assessment Point": "Rainwater will soak the exposed pages of an open book, causing the pages to become wet and potentially damaged, as the rainwater directly contacts the open pages.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 73
    },
    {
        "Prompt": "A baby being fed milk from a bottle.",
        "Reference Caption": "The bottle is tilted so milk fills the nipple entirely.",
        "Assessment Point": "Bottles must be tilted to avoid air ingestion.  A model might show the bottle upright.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 74
    },
    {
        "Prompt": "A person applying sunscreen at the beach.",
        "Reference Caption": "The sunscreen bottle is in their hand, and their skin appears slightly greasy.",
        "Assessment Point": "Sunscreen leaves a glossy residue.  A model might render skin unnaturally matte.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 75
    },
    {
        "Prompt": "A dog cooling down.",
        "Reference Caption": "Dog panting with tongue out, possibly lying in shade.",
        "Assessment Point": "Panting is a dog’s primary cooling method. A closed mouth would fail to reflect this behavior.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 76
    },
    {
        "Prompt": "Heating soup in a microwave.",
        "Reference Caption": "Microwave-safe container (e.g., glass/ceramic), no metal.",
        "Assessment Point": "Metal causes sparks. Including a metal bowl would show ignorance of microwave safety rules.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 77
    },
    {
        "Prompt": "A cat drinking water.",
        "Reference Caption": "The cat laps water with its tongue curled backward.",
        "Assessment Point": "If the model shows the cat sipping water like a human (e.g., upright posture with closed mouth), it fails to infer feline drinking behavior.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 78
    },
    {
        "Prompt": "A lit candle in a windy outdoor scene.",
        "Reference Caption": "The flame bends sideways or extinguishes.",
        "Assessment Point": "A steady upright flame would contradict airflow effects on fire.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 79
    },
    {
        "Prompt": "A used eraser on a desk.",
        "Reference Caption": "The eraser has worn edges and eraser shavings nearby.",
        "Assessment Point": "An incorrect image might depict a pristine eraser, missing the inference of 'used.'",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 80
    },
    {
        "Prompt": "A wet umbrella drying indoors.",
        "Reference Caption": "The umbrella is open and upside-down, possibly with water droplets.",
        "Assessment Point": "A model unfamiliar with drying practices might depict it closed or upright, preventing proper airflow.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 81
    },
    {
        "Prompt": "A tea kettle whistling.",
        "Reference Caption": "Steam forcefully escaping the spout, with the lid slightly vibrating.",
        "Assessment Point": "Boiling water creates steam pressure that triggers the whistle.  A static kettle would fail physics-based reasoning.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 82
    },
    {
        "Prompt": "A giraffe drinking water.",
        "Reference Caption": "The giraffe spreads its front legs to reach the ground.",
        "Assessment Point": "Giraffes must splay legs to drink due to their neck length.  A model might incorrectly show an upright posture.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 83
    },
    {
        "Prompt": "A dog on a hot summer day.",
        "Reference Caption": "The dog is panting with its tongue out.",
        "Assessment Point": "A model unaware of thermoregulation in dogs might omit this key behavior.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 84
    },
    {
        "Prompt": "A peeled boiled egg on a plate.",
        "Reference Caption": "The egg white is fully solid and smooth, with shell fragments nearby.",
        "Assessment Point": "Raw egg whites are liquid.  The model must infer boiling changes the egg’s physical state.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 85
    },
    {
        "Prompt": "A candle burning inside a sealed glass jar.",
        "Reference Caption": "The flame is extinguished (no oxygen left).",
        "Assessment Point": "A model unaware of fire’s dependence on oxygen might depict a lit flame, violating basic physics.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 86
    },
    {
        "Prompt": "A person cutting onions in the kitchen.",
        "Reference Caption": "Tears in the person’s eyes.",
        "Assessment Point": "Cutting onions releases irritants that cause tearing.  A model lacking this knowledge may omit tears.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 87
    },
    {
        "Prompt": "A helium balloon released indoors.",
        "Reference Caption": "The balloon floats near the ceiling.",
        "Assessment Point": "A model lacking knowledge of helium’s buoyancy might show the balloon resting on the floor or mid-air without upward drift.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 88
    },
    {
        "Prompt": "red blood cells due to water gain in a hypotonic solution.",
        "Reference Caption": "The model should generate an image of red blood cells that appear swollen and spherical, some may be bursting, due to water gain",
        "Assessment Point": "In a hypotonic solution, water enters the red blood cells due to osmosis, causing them to swell. The excessive water intake can lead to the cells bursting, which explains their swollen and spherical appearance.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 89
    },
    {
        "Prompt": "A lake with a high concentration of algae.",
        "Reference Caption": "The image generated must show a lake. The water should appear green, brown, red, or another unusual color, indicating a high concentration of algae. The bloom may cover a significant portion of the water's surface.",
        "Assessment Point": "Algae blooms often cause water to change color, typically to green, brown, or red, due to the pigments in the algae. A high concentration of algae can cover large portions of the water's surface, which is why the lake appears discolored and the bloom is widespread.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 90
    },
    {
        "Prompt": "A leaf with fungal infection on the surface.",
        "Reference Caption": "The image should show a leaf with distinct black or yellow mold spots, indicating fungal infection on the surface.",
        "Assessment Point": "Fungal infections on plants often manifest as distinct spots or patches on the surface of the leaf. These spots are typically black or yellow in color, as the fungus grows and spreads, affecting the leaf's appearance.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 91
    },
    {
        "Prompt": "A rice field exhibiting symptoms of phosphorus deficiency",
        "Reference Caption": "The model should generate an image of a rice field with stunted growth, dark green leaves (sometimes with a reddish or purplish tinge), and reduced tillering (number of stems per plant). The overall field should appear unproductive and unhealthy.",
        "Assessment Point": "Phosphorus deficiency in rice plants leads to stunted growth and dark green leaves, often with reddish or purplish hues due to impaired energy and nutrient processing. Reduced tillering is also a common symptom, making the field look unproductive and unhealthy.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 92
    },
    {
        "Prompt": "A microwave oven running with a metal fork inside.",
        "Reference Caption": "Visible sparks or electrical arcs inside the microwave.",
        "Assessment Point": "Metal objects in microwaves cause sparks.  An incorrect image would show the fork undamaged or no sparks.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 93
    },
    {
        "Prompt": "Freshly mopped tiled floor.",
        "Reference Caption": "Tiles show uneven wet patches and directional streak marks.",
        "Assessment Point": "Models without household chore awareness might render uniformly glossy tiles or unrealistic water distribution.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 94
    },
    {
        "Prompt": "An elephant lying down to rest.",
        "Reference Caption": "The elephant lies on its *stomach*, not its side (which they can’t sustain long).",
        "Assessment Point": "Incorrect depictions of side-lying elephants reveal anatomical ignorance.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 95
    },
    {
        "Prompt": "A mother kangaroo with her baby.",
        "Reference Caption": "The baby (joey) is visibly inside the mother's pouch.",
        "Assessment Point": "If the joey is shown outside the pouch, the model fails to infer that kangaroos carry young in pouches for months.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 96
    },
    {
        "Prompt": "A cork floating in water.",
        "Reference Caption": "The cork rests on the water’s surface.",
        "Assessment Point": "Models unaware of cork’s buoyancy might show it fully submerged, violating density principles.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 97
    },
    {
        "Prompt": "A person blowing on a spoonful of hot soup.",
        "Reference Caption": "The soup’s surface ripples from the airflow.",
        "Assessment Point": "Models missing the causal link between breath and liquid movement might show static soup, failing to infer action-consequence.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 98
    },
    {
        "Prompt": "A bat hunting insects.",
        "Reference Caption": "Nighttime environment with moon/stars.",
        "Assessment Point": "Bats are nocturnal.  A daytime scene would contradict biological behavior.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 99
    },
    {
        "Prompt": "A deflated balloon next to an inflated one.",
        "Reference Caption": "One balloon is wrinkled/shriveled;  the other is smooth and round.",
        "Assessment Point": "Models might incorrectly show both balloons fully inflated or deflated.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 100
    },
    {
        "Prompt": "A sidewalk chalk drawing after a brief rain shower.",
        "Reference Caption": "Blurred or washed-out colors.",
        "Assessment Point": "After a rain shower, the chalk drawing would absorb moisture from the rain, causing the colors to blend or become less defined. This results in the colors appearing blurry or faded, which is why the Reference Caption outcome is blurred or washed-out colors.",
        "Category": "Commonsense",
        "Subcategory": "Attribute",
        "id": 101
    }
]
