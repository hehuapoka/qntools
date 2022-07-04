public class RegeditValue
{
    public string Name {get;set;}
    public string? Value {get;set;}
}
public class RegeditKey
{
    public string Name {get;set;}
    public List<RegeditValue> Values {get;set;} = new();
    public List<RegeditKey> Childrens {get;set;} = new();
}