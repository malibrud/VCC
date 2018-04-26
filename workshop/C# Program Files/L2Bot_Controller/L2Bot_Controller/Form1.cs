using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace L2Bot_Controller
{
    public partial class Form1 : Form
    {
        LoCoMoCo mc;

        public Form1()
        {
            InitializeComponent();
            mc = new LoCoMoCo("COM7");
        }

        private void forward_btn_Click(object sender, EventArgs e)
        {
            mc.forward();
        }

        private void left_btn_Click(object sender, EventArgs e)
        {
            mc.turnleft();
        }

        private void right_btn_Click(object sender, EventArgs e)
        {
            mc.turnright();
        }

        private void reverse_btn_Click(object sender, EventArgs e)
        {
            mc.backward();
        }

        private void stop_btn_Click(object sender, EventArgs e)
        {
            mc.stop();
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            mc.close();
            base.OnClosing(e);
        }
    }
}
