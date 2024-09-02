from flask import Flask, render_template, request, redirect, url_for, flash
import create
import converte
import minimiza
import mt
import os
import base

app = Flask(__name__, static_url_path='/static')
pasta_afd = 'static/AFDs/'
pasta_afn = 'static/AFNs/'

caracteres_especiais = "!@#$%&*()-+=<>:;^~.,][}{?/"

# Função para verificar e criar pastas se não existirem
def verifica_pastas():
    pasta_afd = "static/AFDs/"
    pasta_afn = "static/AFNs/"
    if not os.path.exists(pasta_afd):
        os.mkdir(pasta_afd)
    if not os.path.exists(pasta_afn):
        os.mkdir(pasta_afn)

# Rota para a página inicial com o menu
@app.route('/')
def menu():
    verifica_pastas()
    return render_template('menu.html')

# Rota para criar e testar AFNs e AFDs
@app.route('/criar_testar', methods=['GET'])
def criar_testar():
    """
    if request.method == 'POST':
        opcao = request.form.get('opcao')
        if opcao == 'criar_afd':
            return redirect(url_for('criar_afd'))
        elif opcao == 'criar_afn':
            return redirect(url_for('criar_afn'))
        elif opcao == 'testar_linguagem':
            return redirect(url_for('testar_linguagem'))
        else:
            flash('Opção inválida!', 'error')
            return redirect(url_for('menu'))
            """
    return render_template('criar_testar.html')


@app.route('/criar_afd', methods=['GET'])
def render():
    return render_template('criar_afd.html')

@app.route('/monta_afd', methods=['POST'])
def criarafd():
    if request.method == 'POST':
        estados = request.form.get('estados').split(' ')
        alfabeto = request.form.get('alfabeto').split(' ')
        estado_ini = request.form.get('estado_ini')
        estados_finais = request.form.get('estados_finais').split(' ')
        print(request.form.get('transicoes'))

        delta = {}
        for key in request.form:
            if key.startswith('trans_'):
                _, estado, simbolo = key.split('_')
                delta[(estado, simbolo)] = request.form[key].split()
        
        print(request.form['estados'])
        try:
            estados = request.form['estados'].split(' ')
            alfabeto = request.form['alfabeto'].split(' ')
            delta = {}
            estado_ini = request.form['estado_ini']
            estados_finais = request.form['estados_finais'].split(' ')

            for estado in estados:
                for simbolo in alfabeto:
                    chave_transicao = f'trans_{estado}_{simbolo}'
                    print(f'Chave de transição: {chave_transicao}')
                    estado_destino = request.form.get(chave_transicao)
                    if estado_destino:  # Verifica se há um estado de destino válido
                        delta[(estado, simbolo)] = estado_destino.split(' ')
                    else:
                        delta[(estado, simbolo)] = None


            arq_automatoAFN = base.armazena_arquivo(pasta_afd, delta)
            arq_automatoAFN.close()
                
            arqEstados = base.cria_estados(pasta_afd, estados)
            arqEstados.close()

            arq_infoAFD = base.armazena_informacoes(pasta_afd, estado_ini, estados_finais, alfabeto)
            arq_infoAFD.close()

            print(delta)
            delta_lista = base.dict_lista(delta) #convertendo o dicionario em uma lista de tuplas para plotagem.
                
            print(delta_lista)

       
            automato = base.desenhar_automato(estado_ini, estados_finais, delta_lista)
            #image_path = 'AFDs/automatoAFD.png'
            automato.render(os.path.join(pasta_afd, 'automatoAFD'), format='png', cleanup=True)

            #return render_template('criar_afd.html', image_path=image_path, title='Autômato Criado')

        except Exception as e:
            flash(f'Erro ao criar o AFD: {e}')
            return redirect(url_for('criar_afn'))
        
    return redirect(url_for('mostrar_imagemAFD'))


@app.route('/mostrar_imagemAFD')
def mostrar_imagemAFD():
    imagem_url = url_for('static', filename='AFDs/automatoAFD.png')
    return render_template('imagem.html', caminho=imagem_url)

@app.route('/criar_afn', methods=['GET'])
def render2():
    return render_template('criar_afn.html')

@app.route('/monta_afn', methods=['POST'])
def criarafn():
    if request.method == 'POST':
        estados = request.form.get('estados').split(' ')
        alfabeto = request.form.get('alfabeto').split(' ')
        estado_ini = request.form.get('estado_ini')
        estados_finais = request.form.get('estados_finais').split(' ')
        print(request.form.get('transicoes'))

        delta = {}
        for key in request.form:
            if key.startswith('trans_'):
                _, estado, simbolo = key.split('_')
                delta[(estado, simbolo)] = request.form[key].split()
        
        print(request.form['estados'])
        try:
            estados = request.form['estados'].split(' ')
            alfabeto = request.form['alfabeto'].split(' ')
            delta = {}
            estado_ini = request.form['estado_ini']
            estados_finais = request.form['estados_finais'].split(' ')
                    
            for estado in estados:
                for simbolo in alfabeto:
                    chave_transicao = f'trans_{estado}_{simbolo}'
                    print(f'Chave de transição: {chave_transicao}')
                    estado_destino = request.form.get(chave_transicao)
                    if estado_destino != '':  # Verifica se há um estado de destino válido
                        delta[(estado, simbolo)] = estado_destino.split(' ')
                    else:
                        delta[(estado, simbolo)] = None

                    


            arq_automatoAFD = base.armazena_arquivo(pasta_afn, delta)
            arq_automatoAFD.close()
                
            arqEstados = base.cria_estados(pasta_afn, estados)
            arqEstados.close()

            arq_infoAFD = base.armazena_informacoes(pasta_afn, estado_ini, estados_finais, alfabeto)
            arq_infoAFD.close()

            print(delta)
            delta_lista = base.dict_listafront(delta) #convertendo o dicionario em uma lista de tuplas para plotagem.
                
            print(delta_lista)

       
            automato = base.desenhar_automato(estado_ini, estados_finais, delta_lista)
            #image_path = 'AFDs/automatoAFD.png'
            automato.render(os.path.join(pasta_afn, 'automatoAFN'), format='png', cleanup=True)

            #return render_template('criar_afd.html', image_path=image_path, title='Autômato Criado')

        except Exception as e:
            flash(f'Erro ao criar o AFN: {e}')
            return redirect(url_for('criar_afn'))
        
    return redirect(url_for('mostrar_imagemAFN'))


@app.route('/mostrar_imagemAFN')
def mostrar_imagemAFN():
    imagem_url = url_for('static', filename='AFNs/automatoAFN.png')
    return render_template('imagem.html', caminho=imagem_url)


@app.route('/testar_linguagem', methods=['GET', 'POST'])
def testar_linguagem():
    if request.method == 'POST':
        entrada = request.form.get('entrada')
        automato_tipo = request.form.get('automato_tipo')

        try:
            if automato_tipo == 'afd':
                estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afd, '', [], [])
                delta = base.converte_txt_dict(pasta_afd)
                estados_atuais = [estado_ini]
                for simbolo in entrada:
                    novos_estados = []
                    for estado_atual in estados_atuais:
                        prox_estados = delta.get((estado_atual, simbolo), [])
                        novos_estados.extend(prox_estados)
                    estados_atuais = novos_estados

                if any(estado in estados_finais for estado in estados_atuais):
                    resultado = "Reconheceu!"
                else:
                    resultado = "Não reconheceu!"

            elif automato_tipo == 'afn':
                estado_ini, estados_finais, alfabeto = base.push_ini_fini_alfabeto(pasta_afn, '', [], [])
                delta = base.converte_txt_dict(pasta_afn)
                estados_atuais = [estado_ini]
                for simbolo in entrada:
                    novos_estados = []
                    for estado_atual in estados_atuais:
                        prox_estados = delta.get((estado_atual, simbolo), [])
                        novos_estados.extend(prox_estados)
                    estados_atuais = novos_estados

                if any(estado in estados_finais for estado in estados_atuais):
                    resultado = "Reconheceu!"
                else:
                    resultado = "Não reconheceu!"

            else:
                flash('Tipo de autômato inválido.')
                return redirect(url_for('testar_linguagem'))

            return render_template('resultado_teste.html', resultado=resultado)

        except Exception as e:
            flash(f'Erro ao testar a linguagem: {e}')
            return redirect(url_for('testar_linguagem'))

    return render_template('testar_linguagem.html')
    
@app.route('/converter_afn_afd', methods=['GET'])
def converter_afn_afd():
    #diretorio = 'static/AFDs'
    #afds = lista_arquivos(diretorio)
    converte.converte_afn_afd()
    return redirect(url_for('mostrar_imagemConvertido'))

@app.route('/mostrar_imagemConvertido')
def mostrar_imagemConvertido():
    imagem_url = url_for('static', filename='AFDs/automatoConvertido.png')
    return render_template('imagem.html', caminho=imagem_url)

"""
@app.route('/converte_afn_afd', methods=['POST'])
def converter_afn_afd():
    if request.method == 'POST':
        try:
            converte.converte_afn_afd()
            imagem_url = url_for('static', filename='AFDs/AutomatoConvertido.png')
            return render_template('converter_afn_afd.html', caminho=imagem_url)
        
        except Exception as e:
            flash(f'Erro ao converter AFN para AFD: {e}')
            return redirect(url_for('menu'))
        
    return render_template('mostrarImagemConvertido')

@app.route('/mostrarImagemConvertido')
def mostrar_imagemConvertido():
    imagem_url = url_for('static', filename='AFDs/automatoConvertido.png')
    return render_template('imagem.html', caminho=imagem_url)
"""

@app.route('/minimizar_afd', methods=['GET'])
def minimizar_afd():
    minimiza.minimiza_afd()
    return redirect(url_for('mostrar_imagemMinimizado'))

@app.route('/mostrar_imagemMinimizado')
def mostrar_imagemMinimizado():
    imagem_url = url_for('static', filename='AFDs/AutomatoMinimizado.png')
    return render_template('imagem.html', caminho=imagem_url)
      


@app.route('/maquina_turing')
def maquina_turing():
    mt.maquina_turing()
    return redirect(url_for('menu'))


@app.route('/sair')
def sair():
    return "Fechando... Adeus =D"

@app.route('/processar_opcao', methods=['POST'])
def processar_opcao():
    opcao = request.form.get('opcao')

    if opcao == 'criar_afd':  
        create.create_afnafd(caracteres_especiais)
    elif opcao == 'criar_afn':
        create.create_afnafd(caracteres_especiais)
    elif opcao == 'testar_linguagem':
        create.create_afnafd(caracteres_especiais)
    return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(debug=True)