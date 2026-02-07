"""
Roleplay Configuration - Edit these values for your project.

This is the ONLY file you need to edit for hook customization.
Set MC_NAME and CHARACTER_POV at minimum. Other fields are used
by the system when creating sessions and character sheets.
"""

# =============================================================================
# REQUIRED - You must set these
# =============================================================================

# Your MC's name (the character YOU play)
MC_NAME = "MC"

# POV instruction - who Claude writes as
# Examples: "Elena", "the female characters", "all NPCs"
CHARACTER_POV = "the NPCs"

# =============================================================================
# OPTIONAL - Add project-specific coaching agents
# =============================================================================

# Format: [("agent-name", "Brief description"), ...]
COACHING_AGENTS = [
    # ("romance-coach", "Guide romantic tension and pacing"),
    # ("combat-advisor", "Choreograph action scenes"),
]
