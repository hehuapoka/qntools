using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace MayaTaskManager
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public List<MayaTask> list;
        public MainWindow()
        {
            InitializeComponent();
            list = new List<MayaTask>();
#if DEBUG
            list.Add(new MayaTask() { Args=@"D:\a.py"});
            list.Add(new MayaTask() { Args = @"D:\b.py" });
            list.Add(new MayaTask() { Args = @"D:\c.py" });
#endif
            listbox.ItemsSource = list;
        }
    }
}
