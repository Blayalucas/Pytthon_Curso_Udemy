# SubProcess


"""
Usado subprocess para executar e comandos eternos  

O método mais simples para atingir o objetivo é usando subprocess.run().

# stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# returncode -> verifica se tem um erro 
# capture_output -> captura a saída e erro para uso posterior
# text -> Converte o texto 
# shell -> Se True, terá acesso ao shell do sistema. Ao usar
shell (True), recomendo enviar o comando e os argumentos juntos.

Windows: ping 127.0.0.1 


"""

import subprocess

cmd = ['ping','127.0.0.1']

sub = subprocess.run(
    cmd
    
)

print(sub.args)
print(sub.stdout)
print(sub.stderr)
print(sub.returncode)