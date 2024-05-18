from langchain_core.prompts import PromptTemplate

examples = [
    {
        "scene": "A raining forest in sunset",
        "description": "As the sun sets behind the thick canopy, gentle rain showers create a serene ambiance in the forest.\n The golden hues of dusk mingle with the cool tones of rain, painting a tranquil scene."
    },
    {
        "scene": "A mountainous terrain at sunrise",
        "description": "As the first light of dawn crests over the rugged peaks,\n the mountainous terrain is bathed in a warm, amber glow. Shadows dance across the rocky slopes, revealing the contours of the land."
    },
    {
        "scene": "A green plain with wind",
        "description": "Across the vast expanse of the green plain, a steady wind sweeps through the tall grasses,\n causing them to sway in graceful undulations. The air is crisp and invigorating, carrying the scent of wildflowers."
    },
    {
        "scene": "A dark forest",
        "description": "Within the depths of the dark forest, ancient trees loom overhead,\n their gnarled branches casting eerie shadows on the forest floor. The air is thick with mystery, and every rustle of leaves hints at unseen secrets."
    },
    {
        "scene": "A lake at sunrise",
        "description": "As the sun rises above the tranquil lake, its golden rays dance upon the rippling surface,\n painting the water with hues of pink and orange. The gentle lapping of waves against the shore creates a soothing melody."
    },
]

example_template = """
scene: {scene}
description: {description}
"""

example_prompt = PromptTemplate(
    input_variables=["scene", "description"],
    template=example_template
)

prefix = """
The following are exerts of descriptions of scenarios for a rpg.
Use them as examples to describe the last scene, and don't create 
your own scenes.
Using an max o 50 words.
"""

suffix = """
scene: {scene}
description:
"""
