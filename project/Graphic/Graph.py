try:
    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.offline as pyo  
except:
    import subprocess
    subprocess.call(["pip", "install", "plotly"])
    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.offline as pyo
    plotly.tools.set_credentials_file(username='juniorjrc', api_key='tbDLwM4ek5BTeZdR8e1r')
    
import matplotlib.pyplot as plt
pyo.init_notebook_mode()
class Graph():    
    def plotNormalGraph(self,tituloGrafico, labelX, labelY, eixoX1, eixoY1,name1, cor):
        trace0 = go.Bar(
            x=eixoX1,
            y=eixoY1,
            name=name1,
            marker=dict(
                color=cor,)
        )

        data = [trace0]

        #DEFINE O LAYOUT DO GRÁFICO
        layout = go.Layout(
            title=tituloGrafico,
                xaxis=dict(
                    title=labelX,
                    tickangle=-45,
                    tickfont=dict(
                        size=14,
                    )
                ),
                yaxis=dict(
                    title=labelY,
                    tickfont=dict(
                        size=14
                    )
                )
        )

        #RETORNA A PLOTAGEM DO GRÁFICO
        fig = go.Figure(data=data, layout=layout)
        return py.iplot(fig, filename='color-bar')

    def plotComparativeGraph(self,tituloGrafico, labelX, eixoX1, eixoY1,name1, labelY, eixoX2, eixoY2, name2):
        #PRIMEIRA INFORMAÇÃO [PRODUTIVIDADE POLICIAL]
        trace0 = go.Bar(
            x=eixoX1,
            y=eixoY1,
            name=name1,
            marker=dict(
                color='rgba(38, 96, 220, 0.7)'),
        )
        #SEGUNDA INFORMAÇÃO [OCORRENCIAS REGISTRADAS]
        trace1 = go.Bar(
            x=eixoX2,
            y=eixoY2,
            name=name2,
            marker=dict(
                color='rgba(195, 55, 64, 0.7)'),
        )

        data = [trace0, trace1]

        #DEFINE O LAYOUT DO GRÁFICO
        layout = go.Layout(
            title=tituloGrafico,
                xaxis=dict(
                    title=labelX,
                    tickfont=dict(
                        size=14,
                    )
                ),
                yaxis=dict(
                    title=labelY,
                    tickfont=dict(
                        size=14
                    )
                ),
            barmode='group',
            bargap=0.15,
            bargroupgap=0.1
        )

        #RETORNA A PLOTAGEM DO GRÁFICO
        fig = go.Figure(data=data, layout=layout)
        return py.iplot(fig, filename='color-bar')

    def plotPizzaGraph(self, nomes, valores, titulo):
        trace = go.Pie(labels=nomes, values=valores, title=titulo)

        return py.iplot([trace], filename='basic_pie_chart')

    def plotHorizontalGraph(self, tituloGrafico, labelX, labelY, eixoX, eixoY, cor):
        trace0 = go.Bar(
            x=eixoX,
            y=eixoY,
            marker=dict(
                color=cor,),
            orientation='h'
        )

        data = [trace0]

        #DEFINE O LAYOUT DO GRÁFICO
        layout = go.Layout(
            title=tituloGrafico,
                xaxis=dict(
                    title=labelX
                ),
                yaxis=dict(
                    title=labelY
                ),
                margin=dict(
                    l=370
                )
        )
        #RETORNA A PLOTAGEM DO GRÁFICO
        fig = go.Figure(data=data, layout=layout)
        return py.iplot(fig, filename='color-bar')