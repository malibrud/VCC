using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Emgu.CV.Structure;
using Emgu.CV;
using Emgu.Util;

namespace BlackWhiteRed
{
    public partial class Form1 : Form
    {
        Capture _capture = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _capture = new Capture();
            _capture.ImageGrabbed += _capture_ImageGrabbed;
            _capture.Start();
        }

        void _capture_ImageGrabbed(object sender, EventArgs e)
        {
            Image<Gray, byte> bw_image = _capture.RetrieveGrayFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);
            bw_image = bw_image.ThresholdBinary(new Gray(175), new Gray(255));
            Image<Bgr, Byte> color_image = _capture.RetrieveBgrFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);
            Image<Bgr, Byte> final = bw_image.Convert<Bgr, Byte>();

            for (int h = 0; h < color_image.Height; h++)
            {
                for (int w = 0; w < color_image.Width; w++)
                {
                    if (color_image.Data[h, w, 2] > (color_image.Data[h, w, 0] + color_image.Data[h, w, 1] + 30))
                    {
                        final.Data[h, w, 0] = 0;
                        final.Data[h, w, 1] = 0;
                        final.Data[h, w, 2] = 255;
                    }
                }
            }
            imageBox1.Image = final;
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            _capture.Stop();
            base.OnClosing(e);
        }
    }
}
