from huggingface_hub import InferenceClient

hf_token = "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"

def correct_text(question, answer):
    prompt = f"""<s>[INST] Tu es un enseignant qui doit évaluer la réponse d'un étudiant.
    Question posée à l'étudiant : "{question}"
    Réponse de l'étudiant : "{answer}"
    Évalue cette réponse en suivant exactement ce format :
    <b>Compréhension</b>
    <p>[Analyse si la réponse correspond à la question posée]</p>
    <b>Vocabulaire</b>
    <p>[Analyse du vocabulaire utilisé]</p>
    <b>Grammaire</b>
    <p>[Corrections nécessaires OU "Le texte est correct. Félicitations !"]</p>
    <b>Appréciation générale</b>
    <p>[Bref commentaire encourageant]</p>
    Importante: Évalue uniquement le texte fourni, sans le réécrire ni en générer un nouveau.[/INST]</s>
"""
    
    client = InferenceClient(
        model="meta-llama/Meta-Llama-3-70B-Instruct", 
        token=hf_token
        )
    output = client.text_generation(
        prompt, 
        max_new_tokens=4000
        )
    return output