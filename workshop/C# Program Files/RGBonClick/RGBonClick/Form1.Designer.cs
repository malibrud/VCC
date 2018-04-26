namespace RGBonClick
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.imageBox1 = new Emgu.CV.UI.ImageBox();
            this.label1 = new System.Windows.Forms.Label();
            this.red_lbl = new System.Windows.Forms.Label();
            this.green_lbl = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.blue_lbl = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // imageBox1
            // 
            this.imageBox1.Location = new System.Drawing.Point(13, 13);
            this.imageBox1.Name = "imageBox1";
            this.imageBox1.Size = new System.Drawing.Size(259, 194);
            this.imageBox1.TabIndex = 2;
            this.imageBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(105, 220);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(30, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Red:";
            // 
            // red_lbl
            // 
            this.red_lbl.AutoSize = true;
            this.red_lbl.Location = new System.Drawing.Point(146, 220);
            this.red_lbl.Name = "red_lbl";
            this.red_lbl.Size = new System.Drawing.Size(22, 13);
            this.red_lbl.TabIndex = 4;
            this.red_lbl.Text = "- - -";
            // 
            // green_lbl
            // 
            this.green_lbl.AutoSize = true;
            this.green_lbl.Location = new System.Drawing.Point(146, 233);
            this.green_lbl.Name = "green_lbl";
            this.green_lbl.Size = new System.Drawing.Size(22, 13);
            this.green_lbl.TabIndex = 6;
            this.green_lbl.Text = "- - -";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(105, 233);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(39, 13);
            this.label4.TabIndex = 5;
            this.label4.Text = "Green:";
            // 
            // blue_lbl
            // 
            this.blue_lbl.AutoSize = true;
            this.blue_lbl.Location = new System.Drawing.Point(146, 246);
            this.blue_lbl.Name = "blue_lbl";
            this.blue_lbl.Size = new System.Drawing.Size(22, 13);
            this.blue_lbl.TabIndex = 8;
            this.blue_lbl.Text = "- - -";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(105, 246);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(31, 13);
            this.label6.TabIndex = 7;
            this.label6.Text = "Blue:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 274);
            this.Controls.Add(this.blue_lbl);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.green_lbl);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.red_lbl);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.imageBox1);
            this.Name = "Form1";
            this.Text = "RGB On Click";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Emgu.CV.UI.ImageBox imageBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label red_lbl;
        private System.Windows.Forms.Label green_lbl;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label blue_lbl;
        private System.Windows.Forms.Label label6;
    }
}

