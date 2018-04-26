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

namespace OpenCV_Line_Following
{
    public partial class Form1 : Form
    {
        Capture _capture = null;
        LoCoMoCo mc = null;
        int previous_motor_command = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mc = new LoCoMoCo("COM6");
            _capture = new Capture();
            _capture.ImageGrabbed += _capture_ImageGrabbed;
            _capture.Start();
        }

        void _capture_ImageGrabbed(object sender, EventArgs e)
        {
            Image<Bgr, Byte> color_img = _capture.RetrieveBgrFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);
            Image<Gray, Byte> bw_img = _capture.RetrieveGrayFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);
            

            bw_img = bw_img.ThresholdBinary(new Gray(150), new Gray(255)); // if a gray pixel > threshold, then 255; Otherwise 0.
            imageBox1.Image = bw_img.Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR);

            int width = bw_img.Width;
            int height = bw_img.Height;
            int left_col = 0;
            int middle_col = 0;
            int right_col = 0;
            int col_width = width / 3;

            for (int h = 0; h < height; h++)
            {
                for (int w = 0; w < width; w++)
                {
                    if (bw_img.Data[h, w, 0] == 255)
                    {
                        if (w < col_width)
                        {
                            left_col++;
                        }
                        else if (w < (col_width * 2))
                        {
                            middle_col++;
                        }
                        else
                        {
                            right_col++;
                        }
                    }
                }
            }


            byte[, ,] color_data = color_img.Data;
            for (int h = 0; h < height; h++)
            {
                for (int w = 0; w < width; w++)
                {
                    if ((color_data[h, w, 0] > 50 && color_data[h, w, 0] < 90 && // Blue
                        color_data[h, w, 1] > 70 && color_data[h, w, 1] < 110 &&  // Green
                        color_data[h, w, 2] > 210 && color_data[h, w, 2] < 255) // Red
                        || (bw_img.Data[h, w, 0] == 255))
                    {
                        if (w < col_width)
                        {
                            left_col++;
                        }
                        else if (w < (col_width * 2))
                        {
                            middle_col++;
                        }
                        else
                        {
                            right_col++;
                        }
                    }
                }
            }


            int current_motor_command = 0;
            // Send motor command
            if ((left_col > middle_col) && (left_col > right_col))
            {
                current_motor_command = 2; // Turn right
            }
            else if ((right_col > middle_col) && (right_col > left_col))
            {
                current_motor_command = 1; // Turn left
            }
            else
            {
                current_motor_command = 3; // Go forward
            }

            if (current_motor_command != previous_motor_command)
            {
                previous_motor_command = current_motor_command;
                switch (current_motor_command)
                {
                    case 1:
                        mc.turnleft();
                        break;
                    case 2:
                        mc.turnright();
                        break;
                    case 3:
                        mc.forward();
                        break;
                }
            }
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            _capture.Stop();
            base.OnClosing(e);
        }
    }
}
