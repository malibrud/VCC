using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.Util;

namespace RGBonClick
{
    public partial class Form1 : Form
    {

        Capture _capture = null;
        Image<Bgr, Byte> color_img = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _capture = new Capture();
            _capture.ImageGrabbed += _capture_ImageGrabbed;
            _capture.Start();

            imageBox1.MouseClick += new MouseEventHandler(imageBox1_MouseClick);
        }

        void imageBox1_MouseClick(object sender, MouseEventArgs e)
        {
            red_lbl.Text = color_img[e.Location.Y, e.Location.X].Red.ToString();
            green_lbl.Text = color_img[e.Location.Y, e.Location.X].Green.ToString();
            blue_lbl.Text = color_img[e.Location.Y, e.Location.X].Blue.ToString();
        }

        void _capture_ImageGrabbed(object sender, EventArgs e)
        {
            color_img = _capture.RetrieveBgrFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);
            imageBox1.Image = color_img;
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            _capture.Stop();
            base.OnClosing(e);
        }
    }
}
