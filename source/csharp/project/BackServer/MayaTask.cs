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
        public MayaTask(ref Process pc)
        {
            Proc = pc;
        }
        public string Id { get;} = Guid.NewGuid().ToString();
        public string Name { get; set; } = "Default";
        public MayaTaskStatus Status
        {
            get
            {
                if (GetStatus())
                    return MayaTaskStatus.Success;
                else
                    return MayaTaskStatus.Runining;
            }
        }

        private Process?  Proc;

        public bool GetStatus()
        {
           if(Proc != null)
            {
                return !Proc.HasExited;
            }
            return false;

        }
        
    }
}
