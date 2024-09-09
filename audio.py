import whisper
from PyQt5 import QtWidgets, uic



def upload_audio():
    opcoes = QtWidgets.QFileDialog.Options()
    caminho_audio, _ = QtWidgets.QFileDialog.getOpenFileName(
        janela_principal, 
        "Selecionar Arquivo de Áudio", 
        "", 
        "Arquivos de Áudio (*.wav *.m4a);;Todos os Arquivos (*)", 
        options=opcoes
    )

    if caminho_audio:
        janela_principal.textEdit.setText(f'Arquivo selecionado: {caminho_audio}')
        janela_principal.caminhoArquivoAudio = caminho_audio
#hasattr verifica se o objeto tem algo especificado atribuido


def transcrever_audio():
    if not hasattr(janela_principal, 'caminhoArquivoAudio') or not janela_principal.caminhoArquivoAudio:
            janela_principal.textEdit.setText('Nenhum arquivo selecionado.')
            return
    try:
        modelo = whisper.load_model("small")
        resultado = modelo.transcribe(janela_principal.caminhoArquivoAudio)
        texto = resultado['text']
        janela_principal.textEdit.setText(texto)
    except Exception as e:
        janela_principal.textEdit.setText(f'Erro: {str(e)}')






app = QtWidgets.QApplication([])  
janela_principal = uic.loadUi("arquivo.ui")
janela_principal.pushButton.clicked.connect(upload_audio)
janela_principal.pushButton_2.clicked.connect(transcrever_audio)
janela_principal.show()
app.exec_()