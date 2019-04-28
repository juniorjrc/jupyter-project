#IGNORA OS WARNINGS ORIUNDOS DO JUPYTER
import warnings
warnings.filterwarnings('ignore')

try:
    from IPython.html import widgets
    from IPython.display import display
except:
    import subprocess
    subprocess.call(["pip", "install", "IPython"])

class Interface():
    def selecionarAno(self):
        ano = {"2017": 1, "2018": 2, "2019": 3}

        dropdown = widgets.Dropdown(options=ano, description='ANO :', style={'description_width': 'initial'}, layout={'width': '100'})
        return dropdown

    def selecionarFiltro(self):
        filtro = {"PRODUTIVIDADE POLICIAL": 1, "OCORRÊNCIAS REGISTRADAS": 2}

        dropdown = widgets.Dropdown(options=filtro, description='FILTRO :', style={'description_width': 'initial'}, layout={'width': '100'})
        return dropdown
    
    def selecionarCidade(self):
        cidade = {"CRUZEIRO": 1}

        dropdown = widgets.Dropdown(options=cidade, description='CIDADE :', style={'description_width': 'initial'}, layout={'width': '100'})
        return dropdown
    
    def selecionarMes(self):
        mes = {"JANEIRO": 1, "FEVEREIRO": 2, "MARÇO": 3, "ABRIL": 4, "MAIO": 5, "JUNHO": 6, "JULHO": 7, "AGOSTO": 8, "SETEMBRO": 9, "OUTUBRO": 10, "NOVEMBRO": 11, "DEZEMBRO": 12}

        dropdown = widgets.Dropdown(options=mes, description='MẼS :', style={'description_width': 'initial'}, layout={'width': '100'})
        return dropdown
    
    def selecionarNatureza(self, id_filtro):
        if id_filtro == 1:
            natureza = {"OCORRÊNCIAS DE PORTE DE ENTORPECENTES": 1,
             "OCORRÊNCIAS DE TRÁFICO DE ENTORPECENTES": 2,
              "OCORRÊNCIAS DE APREENSÃO DE ENTORPECENTES(1)": 3,
               "OCORRÊNCIAS DE PORTE ILEGAL DE ARMA": 4,
                "Nº DE ARMAS DE FOGO APREENDIDAS": 5,
                 "Nº DE FLAGRANTES LAVRADOS": 6,
                  "Nº DE INFRATORES APREENDIDOS EM FLAGRANTE": 7,
                   "Nº DE INFRATORES APREENDIDOS POR MANDADO": 8,
                    "Nº DE PESSOAS PRESAS EM FLAGRANTE": 9,
                     "Nº DE PESSOAS PRESAS POR MANDADO": 10,
                      "Nº DE PRISÕES EFETUADAS": 11,
                       "Nº DE VEÍCULOS RECUPERADOS": 12}

            dropdown = widgets.Dropdown(options=natureza, description='NATUREZA :', style={'description_width': 'initial'}, layout={'width': 'initial'})
            return dropdown
            
        if id_filtro == 2:
            natureza = {"HOMICÍDIO DOLOSO (2)": 13,
             "FEVERENº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)": 14,
              "HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO": 15,
               "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO": 16,
                "HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO": 17,
                 "HOMICÍDIO CULPOSO OUTROS": 18,
                  "TENTATIVA DE HOMICÍDIO": 19,
                   "LESÃO CORPORAL SEGUIDA DE MORTE": 20,
                    "LESÃO CORPORAL DOLOSA": 21,
                     "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO": 22,
                      "LESÃO CORPORAL CULPOSA - OUTRAS": 23,
                       "LATROCÍNIO": 24,
                       "Nº DE VÍTIMAS EM LATROCÍNIO": 25,
                       "TOTAL DE ESTUPRO (4)": 26,
                       "ESTUPRO": 27,
                       "ESTUPRO DE VULNERÁVEL": 28,
                       "TOTAL DE ROUBO - OUTROS (1)": 29,
                       "ROUBO - OUTROS": 30,
                       "ROUBO DE VEÍCULO": 31,
                       "ROUBO A BANCO": 32,
                       "ROUBO DE CARGA": 33,
                       "FURTO - OUTROS": 34,
                       "FURTO DE VEÍCULO": 35}

            dropdown = widgets.Dropdown(options=natureza, description='NATUREZA :', style={'description_width': 'initial'}, layout={'width': 'initial'})
            return dropdown

        
