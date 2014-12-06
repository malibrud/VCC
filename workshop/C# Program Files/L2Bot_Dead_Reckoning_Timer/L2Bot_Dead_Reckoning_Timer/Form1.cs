using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace L2Bot_Dead_Reckoning_Timer
{
    public partial class Form1 : Form
    {
        LoCoMoCo mc;
        bool running = false;
        Timer tmr = null;
        int tmr_state = 0;

        public Form1()
        {
            InitializeComponent();
            mc = new LoCoMoCo("COM7");
            tmr = new Timer();
            tmr.Tick += new EventHandler(tmr_Tick);
            tmr.Enabled = false;
        }

        private void start_stop_btn_Click(object sender, EventArgs e)
        {
            if (running == false)
            {
                running = true;
                start_stop_btn.Text = "Stop";
                tmr_state = 0;
                tmr.Interval = 5000;
                mc.forward();
                tmr.Enabled = true;
                tmr.Start();
            }
            else
            {
                start_stop_btn.Text = "Start";
                running = false;
                mc.stop();
                tmr.Stop();
                tmr.Enabled = false;
            }
        }

        void tmr_Tick(object sender, EventArgs e)
        {
            tmr.Stop();
            switch (tmr_state)
            {
                // Begin turning
                case 0:
                    mc.turnleft();
                    tmr.Interval = 3000;
                    tmr.Start();
                    tmr_state++;
                    break;
                case 1:
                    mc.forward();
                    tmr.Interval = 5000;
                    tmr.Start();
                    tmr_state++;
                    break;
                case 2:
                    mc.stop();
                    tmr_state = 0;
                    start_stop_btn.Text = "Start";
                    running = false;
                    tmr.Stop();
                    tmr.Enabled = false;
                    break;
            }
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            mc.close();
            base.OnClosing(e);
        }
    }
}
