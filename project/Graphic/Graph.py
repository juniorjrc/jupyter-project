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
    plotly.tools.set_credentials_file(username='juniorjrcsccp', api_key='l7nnf1WZwE7AJ3kIXxP6')
    
import matplotlib.pyplot as plt
pyo.init_notebook_mode()
class Graph():    
    def plotNormalGraph(self,tituloGrafico, labelX, labelY, eixoX1, eixoY1,name1, cor, nomeArquivo):
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
        return py.iplot(fig, filename=nomeArquivo)

    def plotComparativeGraph(self,tituloGrafico, labelX, eixoX1, eixoY1,name1, labelY, eixoX2, eixoY2, name2, nomeArquivo):
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
        return py.iplot(fig, filename=nomeArquivo)

    def plotPizzaGraph(self, nomes, valores, titulo, nomeArquivo):
        trace = go.Pie(labels=nomes, values=valores, title=titulo)

        return py.iplot([trace], filename=nomeArquivo)

    def plotHorizontalGraph(self, tituloGrafico, labelX, labelY, eixoX, eixoY, cor, nomeArquivo):
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
        return py.iplot(fig, filename=nomeArquivo)

    def plotHorizontalComparativeGraph(self,tituloGrafico, labelX, labelY, y1, x1, nam1, cor1, y2, x2, nam2, cor2, y3, x3, nam3, cor3, nomeArquivo):
        trace1 = go.Bar(
            y=y1,
            x=x1,
            name=nam1,
            orientation = 'h',
            marker = dict(
                color = cor1,
            )
        )
        trace2 = go.Bar(
            y=y2,
            x=x2,
            name=nam2,
            orientation = 'h',
            marker = dict(
                color = cor2,
            )
        )
        trace3 = go.Bar(
            y=y3,
            x=x3,
            name=nam3,
            orientation = 'h',
            marker = dict(
                color = cor3,
            )
        )

        data = [trace1, trace2, trace3]
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
                ),
            barmode='stack'
        )
        fig = go.Figure(data=data, layout=layout)
        return py.iplot(fig, filename=nomeArquivo)