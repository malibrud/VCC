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

namespace OpenCV_Pixel_Counter
{
    public partial class Form1 : Form
    {

        Capture _capture = null;
        int threshold = 150;
        public Form1()
        {
            InitializeComponent();
            this.KeyPreview = true;
            this.KeyDown += new KeyEventHandler(Form1_KeyDown);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _capture = new Capture();
            _capture.ImageGrabbed += _capture_ImageGrabbed;
            _capture.Start();
        }

        void _capture_ImageGrabbed(object sender, EventArgs e)
        {
            Image<Gray, Byte> bw_img = _capture.RetrieveGrayFrame();

            bw_img = bw_img.ThresholdBinary(new Gray(threshold), new Gray(255)); // if a gray pixel > threshold, then 255; Otherwise 0.
            imageBox1.Image = bw_img.Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);

            int width = bw_img.Width;
            int height = bw_img.Height;
            int count = 0;

            for (int h = 0; h < height; h++)
            {
                for (int w = 0; w < width; w++)
                {
                    if (bw_img.Data[h, w, 0] == 255) // Why 0? -- Grayscale image
                    //How to access Image data? Read: http://www.emgu.com/wiki/index.php/Setting_up_EMGU_C_Sharp
                    {
                        count++;
                    }
                }
            }

            if (count > (width * height / 3))
            {
                this.BackColor = Color.Red;
            }
            else
            {
                this.BackColor = Color.Green;
            }
        }

        void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up)
            {
                threshold += 5;
                if (threshold >= 255)
                    threshold = 255;
            }
            else if (e.KeyCode == Keys.Down)
            {
                threshold -= 5;
                if (threshold <= 0)
                    threshold = 0;
            }
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            _capture.Stop();
            base.OnClosing(e);
        }
    }
}
