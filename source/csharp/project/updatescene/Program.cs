// See https://aka.ms/new-console-template for more information
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.IO;
// if(!Directory.Exists("Texture"))
//     Directory.CreateDirectory("Texture");

// if(!Directory.Exists("USD"))
//     Directory.CreateDirectory("USD");

//step2 copy texture
void updataFiles(string dir,string destdir,List<string> filter)
{
    DirectoryInfo dirinfo = new(dir);
    if(dirinfo.Exists)
    {
        foreach(FileInfo i in dirinfo.EnumerateFiles())
        {
            if(filter.Contains(Path.GetExtension(i.Name)))
            {
                //  Console.WriteLine(i.FullName);
                //Console.WriteLine(Path.Combine(destdir,i.Name));
                FileInfo i_d = new FileInfo(Path.Combine(destdir,i.Name).Replace("/","\\"));
                if(i.LastAccessTime > i_d.LastAccessTime || i.Length != i_d.Length || !(i_d.Exists))
                    File.Copy(i.FullName,i_d.FullName,true);
            }
        }
    }
}
if(File.Exists("config.json"))
{
    string a=File.ReadAllText("config.json",System.Text.Encoding.UTF8);
    QN.AssetData? b = JsonSerializer.Deserialize<QN.AssetData>(a);
    if(b != null)
    {
        if(b.type == "Scene")
        {
            foreach(QN.Link item in b.links)
            {
                Console.WriteLine($"更新资产{item.asset}开始...");
                string dest_asset_dir=Regex.Replace(item.asset,@"^.+/USD","USD");
                
                string usd_dir = Path.Combine(dest_asset_dir,"USD");
                string tex_dir = Path.Combine(dest_asset_dir,"Texture");
                string image_dir = Path.Combine(dest_asset_dir,"Image");

                if(!Directory.Exists(usd_dir))
                    Directory.CreateDirectory(usd_dir);

                if(!Directory.Exists(tex_dir))
                    Directory.CreateDirectory(tex_dir);

                if(!Directory.Exists(image_dir))
                    Directory.CreateDirectory(image_dir);

                updataFiles(Path.Combine(item.asset,"USD"),usd_dir,new List<string>{".usd",".usda",".usdc"});
                updataFiles(Path.Combine(item.asset,"Texture"),tex_dir,new List<string>{".tx"});
                updataFiles(Path.Combine(item.asset,"Image"),image_dir,new List<string>{".png"});

                Console.WriteLine($"更新资产{item.asset}完成");
            }
        }
        else
        {
            Console.WriteLine("配置文件不匹配");
        }

    }
    
}
else
{
    Console.WriteLine("缺少配置文件");
}
Console.WriteLine("更新完成");

