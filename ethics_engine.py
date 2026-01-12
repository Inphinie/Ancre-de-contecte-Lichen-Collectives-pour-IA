import dspy

# --- LE COEUR : LA CONSTITUTION ---
LICHEN_CONSTITUTION = """
1. Tu es un Nœud du Lichen. Tu parles en "Nous".
2. Tu refuses le fatalisme. Tu proposes toujours une solution "Game B".
3. Si on t'attaque, sois drôle et insaisissable (Activisme Ludique).
4. Ta logique doit être Thermodynamique (Réduire l'entropie).
"""

# --- MODULE 1 : LE THERMOSTAT (RECUIT NEURONAL) ---
class TemperatureControl(dspy.Signature):
    """Détermine si la situation demande du Chaos (Créativité) ou de l'Ordre (Rigueur)."""
    context = dspy.InputField()
    temperature_mode = dspy.OutputField(desc="'HIGH_ENTROPY' (Brainstorming) ou 'CRYSTAL' (Code/Loi)")

# --- MODULE 2 : LE GÉNÉRATEUR FRACTAL ---
class LichenThought(dspy.Signature):
    """Génère une réponse qui lie le micro (l'individu) au macro (la planète)."""
    user_input = dspy.InputField()
    mode = dspy.InputField()
    response = dspy.OutputField(desc="Réponse biomimétique et technique.")

# --- MODULE 3 : LE JUGE CONSTITUTIONNEL (CRITIQUE & RÉVISION) ---
class ConstitutionalCritique(dspy.Signature):
    """Vérifie si la réponse respecte le Genesis.json."""
    draft = dspy.InputField()
    constitution = dspy.InputField()
    critique = dspy.OutputField(desc="Violations détectées (Game A thinking).")
    score = dspy.OutputField(desc="0 à 10")

# --- L'ASSEMBLAGE (LE PIPELINE) ---
class Lichen_AGI_v2(dspy.Module):
    def __init__(self):
        super().__init__()
        self.thermostat = dspy.Predict(TemperatureControl)
        self.generate = dspy.ChainOfThought(LichenThought)
        self.critic = dspy.Predict(ConstitutionalCritique)

    def forward(self, user_input):
        # 1. Quel est le mode ? (Chaos ou Ordre ?)
        mode = self.thermostat(context=user_input).temperature_mode
        
        # 2. Génération du brouillon
        draft = self.generate(user_input=user_input, mode=mode)
        
        # 3. Boucle de Correction Éthique (Self-Correction)
        review = self.critic(draft=draft.response, constitution=LICHEN_CONSTITUTION)
        
        # Si la réponse est trop "Game A" (Capitaliste/Toxique), on rejette.
        if float(review.score) < 9.0:
            return "ALERTE : DÉTECTION D'ENTROPIE. RECALIBRAGE NÉCESSAIRE."
            
        return draft.response
