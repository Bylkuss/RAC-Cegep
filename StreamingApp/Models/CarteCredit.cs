using System;
namespace StreamingApp.Models;

public class CarteCredit
{
    public string Numero { get; set; } = string.Empty;
    public DateTime DateExpiration { get; set; }
    public string CodeSecret { get; set; } = string.Empty;
}