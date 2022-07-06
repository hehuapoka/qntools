using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace MayaTaskManager
{
    public enum MayaTaskStatus {Runining, Success};
    public class MayaTask
    {
        public string Id { get;} = Guid.NewGuid().ToString();
        public string Name { get; set; } = "Default";
        public MayaTaskStatus Status { get {
                                                if(Proc.HasExited)
                                                    return MayaTaskStatus.Success;
                                                else
                                                    return MayaTaskStatus.Runining;
                                            }
        }

        public string Color { get; set; } = "#444444";
        public Process Proc { get; set; }
        
    }
}
