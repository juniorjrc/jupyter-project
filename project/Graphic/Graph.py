import matplotlib.pyplot as plt
class Graph():
    def plotGraph(self, titulo, xlabel, ylabel, linhax, linhay, cor, tipo, nomeImagem):
        # PLOTA O GRÁFICO
        fig, ax1 = plt.subplots(1, figsize=(10, 10))
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
        ax = plt.gca()
        ax.tick_params(axis = 'both', which = 'major', labelsize = 9)
        #ax.tick_params(axis = 'both', which = 'minor', labelsize = 5)
        ax.patch.set_facecolor('xkcd:dark grey')
        plt.savefig(nomeImagem)
        if tipo == "bar":
            ax1.bar(linhax, linhay, color=cor)
            ax1.set_xticklabels(linhax, rotation=45)
        if tipo == "plot":
            ax1.bar(linhax, linhay, color=cor )
            ax1.set_xticklabels(linhax, rotation=90)
        ax1.set_xticks(linhax)
        ax1.set_yticks(linhay)
        ax1.set_yticklabels(linhay)
        ax1.set_title(titulo)
        plt.show()
