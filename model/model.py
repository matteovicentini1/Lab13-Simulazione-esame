from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idmap={}


    def creagrafo(self,forma,anno):
        nodi = DAO.nodi()
        for i in nodi:
            self.grafo.add_node(i)
            self.idmap[i.id]=i
        archi = DAO.soloarchi()
        for part,arr in archi:
            somma=0
            pesi = DAO.archi(forma,anno,part,arr)
            for i in pesi:
                somma +=i
            self.grafo.add_edge(self.idmap[part],self.idmap[arr],peso=somma)


    def listastati(self):
        lista=[]
        for i in self.grafo.nodes:
            somma=0
            for vic in self.grafo.neighbors(i):
                somma += self.grafo[i][vic]['peso']
            lista.append((i,somma))
        return lista

    def getanni(self):
        return DAO.anni()

    def getforme(self):
        return DAO.forme()

    def getnodi(self):
        return len(self.grafo.nodes)

    def getarchi(self):
        return len(self.grafo.edges)