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

namespace OpenCV_Line_Following_Cone
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
            Image<Gray, Byte> bw_img = _capture.RetrieveGrayFrame().Resize(imageBox1.Width, imageBox1.Height, Emgu.CV.CvEnum.INTER.CV_INTER_LINEAR); ;

            bw_img = bw_img.ThresholdBinary(new Gray(150), new Gray(255)); // if a gray pixel > threshold, then 255; Otherwise 0.

            int width = bw_img.Width;
            int height = bw_img.Height;
            int left_col = 0;
            int middle_col = 0;
            int right_col = 0;
            int red_count = 0;
            int col_width = width / 3;
            byte[, ,] color_data = color_img.Data;

            for (int h = 0; h < height; h++)
            {
                for (int w = 0; w < width; w++)
                {
                    if (color_data[h, w, 0] > 80 && color_data[h, w, 0] < 120 && // Blue
                        color_data[h, w, 1] > 80 && color_data[h, w, 1] < 120 &&  // Green
                        color_data[h, w, 2] > 210 && color_data[h, w, 2] < 255) // Red
                    {
                        color_data[h, w, 0] = 100;
                        color_data[h, w, 1] = 100;
                        color_data[h, w, 2] = 225;
                        red_count++;
                    }
                    else if (bw_img.Data[h, w, 0] == 255)
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
                        color_data[h, w, 0] = 255;
                        color_data[h, w, 1] = 255;
                        color_data[h, w, 2] = 225;
                    }
                    else
                    {
                        color_data[h, w, 0] = 0;
                        color_data[h, w, 1] = 0;
                        color_data[h, w, 2] = 0;
                    }
                }
            }

            int current_motor_command = 500;
            // Send motor command
            if (red_count > 350)
            {
                current_motor_command = 0;
            }
            else if ((left_col > middle_col) && (left_col > right_col))
            {
                current_motor_command = 1;
            }
            else if ((right_col > middle_col) && (right_col > left_col))
            {
                current_motor_command = 2;
            }
            else
            {
                current_motor_command = 3;
            }

            if (current_motor_command != previous_motor_command)
            {
                previous_motor_command = current_motor_command;
                switch (current_motor_command)
                {
                    case 0:
                        mc.stop();
                        break;
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
            imageBox1.Image = color_img;
        }

        protected override void OnClosing(CancelEventArgs e)
        {
            _capture.Stop();
            base.OnClosing(e);
        }
    }
}
