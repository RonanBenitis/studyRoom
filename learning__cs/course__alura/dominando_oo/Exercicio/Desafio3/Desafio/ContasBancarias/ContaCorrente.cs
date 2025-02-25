namespace Desafio.ContasBancarias
{
    internal class ContaCorrente : ContaBancaria
    {
        private double TaxaManutencao { get; set; }

        public override void Sacar(double valor)
        {
            base.Sacar(valor * (TaxaManutencao));
        }
    }
}
