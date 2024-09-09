# TranscricaoAudio
Projeto de Transcrição de Áudio com PyQt5 e Whisper
Este projeto demonstra a criação de uma aplicação desktop para transcrição automática de áudios, desenvolvida utilizando Python. A aplicação combina a biblioteca PyQt5 para a interface gráfica e o modelo de transcrição Whisper da OpenAI, proporcionando uma ferramenta prática e eficaz para converter áudio em texto.

Funcionalidades Principais:
Seleção de Arquivo de Áudio:

Utiliza um diálogo de arquivos para permitir que o usuário selecione um arquivo de áudio no formato .wav ou .m4a.
O caminho do arquivo selecionado é exibido na interface gráfica para confirmação.
Transcrição de Áudio:

Carrega o modelo Whisper "small" para transcrever o áudio selecionado.
Exibe o texto transcrito diretamente na interface gráfica.
Inclui tratamento de erros para garantir que a aplicação lida com problemas como falta de seleção de arquivo ou falhas durante a transcrição.
Observação Importante:
Para executar o projeto, certifique-se de que o arquivo arquivo.ui está na mesma pasta que o executável gerado. Este arquivo é crucial para a interface gráfica e sem ele, a aplicação não funcionará corretamente.
