namespace L2Bot_Controller
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
            this.forward_btn = new System.Windows.Forms.Button();
            this.left_btn = new System.Windows.Forms.Button();
            this.right_btn = new System.Windows.Forms.Button();
            this.reverse_btn = new System.Windows.Forms.Button();
            this.stop_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // forward_btn
            // 
            this.forward_btn.Location = new System.Drawing.Point(98, 23);
            this.forward_btn.Name = "forward_btn";
            this.forward_btn.Size = new System.Drawing.Size(75, 23);
            this.forward_btn.TabIndex = 0;
            this.forward_btn.Text = "FORWARD";
            this.forward_btn.UseVisualStyleBackColor = true;
            this.forward_btn.Click += new System.EventHandler(this.forward_btn_Click);
            // 
            // left_btn
            // 
            this.left_btn.Location = new System.Drawing.Point(17, 62);
            this.left_btn.Name = "left_btn";
            this.left_btn.Size = new System.Drawing.Size(75, 23);
            this.left_btn.TabIndex = 1;
            this.left_btn.Text = "LEFT";
            this.left_btn.UseVisualStyleBackColor = true;
            this.left_btn.Click += new System.EventHandler(this.left_btn_Click);
            // 
            // right_btn
            // 
            this.right_btn.Location = new System.Drawing.Point(179, 62);
            this.right_btn.Name = "right_btn";
            this.right_btn.Size = new System.Drawing.Size(75, 23);
            this.right_btn.TabIndex = 2;
            this.right_btn.Text = "RIGHT";
            this.right_btn.UseVisualStyleBackColor = true;
            this.right_btn.Click += new System.EventHandler(this.right_btn_Click);
            // 
            // reverse_btn
            // 
            this.reverse_btn.Location = new System.Drawing.Point(98, 102);
            this.reverse_btn.Name = "reverse_btn";
            this.reverse_btn.Size = new System.Drawing.Size(75, 23);
            this.reverse_btn.TabIndex = 3;
            this.reverse_btn.Text = "REVERSE";
            this.reverse_btn.UseVisualStyleBackColor = true;
            this.reverse_btn.Click += new System.EventHandler(this.reverse_btn_Click);
            // 
            // stop_btn
            // 
            this.stop_btn.Location = new System.Drawing.Point(98, 62);
            this.stop_btn.Name = "stop_btn";
            this.stop_btn.Size = new System.Drawing.Size(75, 23);
            this.stop_btn.TabIndex = 4;
            this.stop_btn.Text = "STOP";
            this.stop_btn.UseVisualStyleBackColor = true;
            this.stop_btn.Click += new System.EventHandler(this.stop_btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 147);
            this.Controls.Add(this.stop_btn);
            this.Controls.Add(this.reverse_btn);
            this.Controls.Add(this.right_btn);
            this.Controls.Add(this.left_btn);
            this.Controls.Add(this.forward_btn);
            this.Name = "Form1";
            this.Text = "L2Bot Controller";
            this.ResumeLayout(false);
        }

        #endregion

        private System.Windows.Forms.Button forward_btn;
        private System.Windows.Forms.Button left_btn;
        private System.Windows.Forms.Button right_btn;
        private System.Windows.Forms.Button reverse_btn;
        private System.Windows.Forms.Button stop_btn;
    }
}


