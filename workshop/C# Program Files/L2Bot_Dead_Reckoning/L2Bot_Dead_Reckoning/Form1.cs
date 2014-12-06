using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;

namespace L2Bot_Dead_Reckoning
{
    public partial class Form1 : Form
    {
        LoCoMoCo mc;

        public Form1()
        {
            InitializeComponent();
            mc = new LoCoMoCo("COM7");
        }

        private void start_stop_btn_Click(object sender, EventArgs e)
        {
            mc.forward();
            Thread.Sleep(5000); // Drive straight for 5 seconds
            mc.turnleft();
            Thread.Sleep(3000); // Turn left for 3 seconds
            mc.forward();
            Thread.Sleep(5000);  // Drive straight for 5 seconds
            mc.stop();
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            mc.close();
            base.OnClosing(e);
        }
    }
}

