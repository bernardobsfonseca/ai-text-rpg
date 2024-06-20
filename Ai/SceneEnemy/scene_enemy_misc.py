from langchain_core.prompts import PromptTemplate

examples = [
    {
        "scene": "A furious sylph in a rainy forest of pines",
        "description": "In a rain-soaked forest of towering pines, a furious sylph emerges, her eyes gleaming with wrath as she commands the winds. Leaves whirl in her fury, daring brave travelers to calm her inner storm."
    },
    {
        "scene": "A huge ogre in a stormy mountain range",
        "description": "Amidst crashing thunder and swirling clouds atop a stormy mountain range, a huge ogre, towering like a mountain, roars with wrath, challenging any brave enough to face its thunderous might."
    },
    {
        "scene": "A fast imp in a sunny plain",
        "description": "In the vast expanse of a sun-drenched plain, a small but lightning-fast imp, with eyes gleaming mischief, darts between grassy knolls, causing chaos and laughter among the unsuspecting travelers."
    },
    {
        "scene": "A frightening fire salamander in a rainy forest",
        "description": "Beneath the relentless downpour in the dense forest, a frightening fire salamander, its scales glowing ominously in the darkness, stalks alone, its fiery breath illuminating the shadows as it hunts for prey."
    },
    {
        "scene": "A small gnome in a foggy mountain pass by a lake",
        "description": "Within the thick fog clinging to the mountain pass overlooking a tranquil lake, a lone and small gnome, armed with a trusty lantern and a heart full of courage, bravely navigates the misty terrain, wary of the lurking dangers concealed in the haze."
    }
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
The following are exerts of descriptions of encounters scenes with enemys for a rpg.
Use them as examples to describe the last scene, and don't create 
your own scenes.
Using an max o 50 words.
"""

suffix = """
scene: {scene}
description:
"""
