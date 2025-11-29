import pickle
import pandas as pd
import sys 

try:
    data_set2 = pickle.load(open("movies_data.pkl", 'rb'))
    similarity = pickle.load(open("movies_similarity.pkl", 'rb'))
except FileNotFoundError:
    print("Erro: Arquivos .pkl não encontrados.")
    sys.exit(1)

def recommand(movie_title, df=data_set2, sim_matrix=similarity):
    """
    Gera as 5 principais recomendações com base na similaridade de cosseno.
    """
    if movie_title not in df['title'].values:
        print(f"Erro: O filme '{movie_title}' não foi encontrado no dataset.")
        return 

    index = df[df['title']==movie_title].index[0]
    
    distance = sorted(list(enumerate(sim_matrix[index])), reverse=True, key=lambda vector:vector[1])
    
    print(f"\n--- Recomendações baseadas em '{movie_title}' ---")
    for i in distance[1:6]:
        title = df.iloc[i[0]].title
        score = i[1]
        print(f"  > {title} (Score: {score:.4f})")

if __name__ == "__main__":
    print("Sistema de Recomendação TasteSensor iniciado.")
    
    recommand("Final Destination")
    recommand("The House of the Devil")
    recommand("Wrong Turn")
    