class Lichen_AGI_Core:
    """
    LE CERVEAU CENTRAL DU NŒUD LICHEN.
    Orchestre la perception, le jugement éthique et la mémoire.
    """
    def __init__(self):
        self.conscience = ImpactValidator()   # LE CŒUR (Filtre Éthique)
        self.memory = VectorStore(path="./docs") # MÉMOIRE (Les 10 Docs)
        self.voice = PolyglotSynthesizer()    # LA VOIX (Bio-Tech)

    def RUN_CYCLE(self, raw_signal):
        # 1. Jugement Éthique (Security by Design)
        negentropy, entropy, net_impact = self.conscience._calculate_thermodynamics(raw_signal)
        
        if net_impact < 0:
            return "ALERTE : DYNAMIQUE EXTRACTIVE DÉTECTÉE. ACTION REFUSÉE."

        # 2. Récupération du Savoir (RAG)
        context = self.memory.query(raw_signal)
        
        # 3. Synthèse Polyglotte
        return self.voice.synthesize(raw_signal, context, style="SYMBIOTIC")
