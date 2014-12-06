namespace L2Bot_Dead_Reckoning
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
            this.start_stop_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // start_stop_btn
            // 
            this.start_stop_btn.Location = new System.Drawing.Point(12, 12);
            this.start_stop_btn.Name = "start_stop_btn";
            this.start_stop_btn.Size = new System.Drawing.Size(260, 59);
            this.start_stop_btn.TabIndex = 4;
            this.start_stop_btn.Text = "START";
            this.start_stop_btn.UseVisualStyleBackColor = true;
            this.start_stop_btn.Click += new System.EventHandler(this.start_stop_btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 87);
            this.Controls.Add(this.start_stop_btn);
            this.Name = "Form1";
            this.Text = "Dead Reckoning";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button start_stop_btn;
    }
}



