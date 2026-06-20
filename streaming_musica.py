class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.reproducoes = 0
        
    def reproduzir(self):
        self.reproducoes += 1
        
    def get_reproducoes(self):
        return self.reproducoes
        
class Playlist:
    def __init__(self, nome: str, limite_musicas: int):
        self.nome = nome
        self.musicas = []
        self.__limite_musicas = limite_musicas
    
    def adicionar_musica(self, musica):
        if len(self.musicas) < self.__limite_musicas:
            self.musicas.append(musica)
        else:
            ...
            
    def remover_musica(self, titulo):
        self.musicas = [musica for musica in self.musicas if musica.titulo != titulo]
    
    def reproduzir_todas(self):
        for musica in self.musicas:
            musica.reproduzir()
        
    def duracao_total(self):
        duracao = [musica.duracao for musica in self.musicas]
        return sum(duracao)
        
    def buscar_musica(self, titulo):
        for musica in self.musicas:
            if musica.titulo == titulo:
                return musica
        
        return None
    
    def listar_titulos(self):
        return [musica.titulo for musica in self.musicas]
        
    def get_limite(self):
        return self.__limite_musicas
        
    def alterar_limite(self, novo_limite):
        if novo_limite > 0 and novo_limite >= len(self.musicas):
            self.__limite_musicas = novo_limite
        else:
           ...
        