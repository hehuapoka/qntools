using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MayaTaskManager
{
    public enum MayaTaskStatus {Idleing=0,Runining, Success, Failure };
    public class MayaTask
    {
        public string Name { get; set; } = "Default";
        public string Exec { get; set; } = Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION")??"", @"bin\mayapy.exe");
        public string Args { get; set; } = "";
        public MayaTaskStatus Status { get; set; }
        
    }
}
