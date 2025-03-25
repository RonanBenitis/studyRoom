#! /bin/bash
read -p "Entre com a operacao desejada: 'compactar' ou 'descompactar'" operacao
case "$operacao" in
	"compactar")
		read -p "Nome do arquivo final (.tar.gz): " arquivo_saida
		read -p "Caminho dos arquivos a compactar: " caminho
		read -p "Lista de arquivos separados por espaço: " arquivos

		tar -czf "$arquivo_saida" -C "$caminho" $arquivos

		echo "Compactados com sucesso em $arquivo_saida"
	;;
	"descompactar")
		read -p "Qual é o nome do arquivo a ser a descompactar (.tar.gz)" arquivo
		read -p "Diretorio de destino" diretorio

		tar -xzf "$arquivo" -C "$diretorio"

		echo "Descompactado com sucesso em $diretorio"
	;;
	*)
		echo "Operacao invalida!"
		echo "Selecione descompactar ou compactar"
		exit 1
	;;
esac
