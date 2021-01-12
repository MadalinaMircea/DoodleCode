
namespace DoodleRecognizerFront
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.ImagePictureBox = new System.Windows.Forms.PictureBox();
            this.LoadButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.RotateButton = new System.Windows.Forms.Button();
            this.DetectedPanel = new System.Windows.Forms.Panel();
            this.GenerateCodeButton = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.DetectedBoxList = new System.Windows.Forms.CheckedListBox();
            this.MainPanel = new System.Windows.Forms.Panel();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.listBox1 = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).BeginInit();
            this.DetectedPanel.SuspendLayout();
            this.MainPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // ImagePictureBox
            // 
            this.ImagePictureBox.BackColor = System.Drawing.Color.MintCream;
            this.ImagePictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.ImagePictureBox.Location = new System.Drawing.Point(17, 60);
            this.ImagePictureBox.Name = "ImagePictureBox";
            this.ImagePictureBox.Size = new System.Drawing.Size(930, 534);
            this.ImagePictureBox.TabIndex = 0;
            this.ImagePictureBox.TabStop = false;
            // 
            // LoadButton
            // 
            this.LoadButton.BackColor = System.Drawing.Color.Turquoise;
            this.LoadButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadButton.Location = new System.Drawing.Point(368, 600);
            this.LoadButton.Name = "LoadButton";
            this.LoadButton.Size = new System.Drawing.Size(194, 54);
            this.LoadButton.TabIndex = 1;
            this.LoadButton.Text = "Load Picture";
            this.LoadButton.UseVisualStyleBackColor = false;
            this.LoadButton.Click += new System.EventHandler(this.button1_Click);
            this.LoadButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(275, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(287, 32);
            this.label1.TabIndex = 4;
            this.label1.Text = "Choose your picture";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // RotateButton
            // 
            this.RotateButton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("RotateButton.BackgroundImage")));
            this.RotateButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.RotateButton.Enabled = false;
            this.RotateButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RotateButton.Location = new System.Drawing.Point(568, 600);
            this.RotateButton.Name = "RotateButton";
            this.RotateButton.Size = new System.Drawing.Size(60, 54);
            this.RotateButton.TabIndex = 8;
            this.RotateButton.UseVisualStyleBackColor = true;
            this.RotateButton.Click += new System.EventHandler(this.button3_Click);
            // 
            // DetectedPanel
            // 
            this.DetectedPanel.Controls.Add(this.GenerateCodeButton);
            this.DetectedPanel.Controls.Add(this.label4);
            this.DetectedPanel.Controls.Add(this.DetectedBoxList);
            this.DetectedPanel.Location = new System.Drawing.Point(0, 0);
            this.DetectedPanel.Name = "DetectedPanel";
            this.DetectedPanel.Size = new System.Drawing.Size(1187, 687);
            this.DetectedPanel.TabIndex = 14;
            // 
            // GenerateCodeButton
            // 
            this.GenerateCodeButton.BackColor = System.Drawing.Color.Turquoise;
            this.GenerateCodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GenerateCodeButton.Location = new System.Drawing.Point(941, 263);
            this.GenerateCodeButton.Name = "GenerateCodeButton";
            this.GenerateCodeButton.Size = new System.Drawing.Size(222, 133);
            this.GenerateCodeButton.TabIndex = 2;
            this.GenerateCodeButton.Text = "Generate my code!";
            this.GenerateCodeButton.UseVisualStyleBackColor = false;
            this.GenerateCodeButton.Click += new System.EventHandler(this.GenerateCodeButton_Click);
            this.GenerateCodeButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(133, 25);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(495, 32);
            this.label4.TabIndex = 1;
            this.label4.Text = "What objects are of interest to you?";
            // 
            // DetectedBoxList
            // 
            this.DetectedBoxList.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DetectedBoxList.FormattingEnabled = true;
            this.DetectedBoxList.Location = new System.Drawing.Point(17, 79);
            this.DetectedBoxList.Name = "DetectedBoxList";
            this.DetectedBoxList.Size = new System.Drawing.Size(889, 598);
            this.DetectedBoxList.TabIndex = 0;
            this.DetectedBoxList.SelectedIndexChanged += new System.EventHandler(this.DetectedBoxList_SelectedIndexChanged);
            // 
            // MainPanel
            // 
            this.MainPanel.Controls.Add(this.listBox1);
            this.MainPanel.Controls.Add(this.checkBox1);
            this.MainPanel.Controls.Add(this.richTextBox1);
            this.MainPanel.Controls.Add(this.button2);
            this.MainPanel.Controls.Add(this.RotateButton);
            this.MainPanel.Controls.Add(this.label1);
            this.MainPanel.Controls.Add(this.ImagePictureBox);
            this.MainPanel.Controls.Add(this.LoadButton);
            this.MainPanel.Location = new System.Drawing.Point(0, 0);
            this.MainPanel.Name = "MainPanel";
            this.MainPanel.Size = new System.Drawing.Size(1184, 684);
            this.MainPanel.TabIndex = 3;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(962, 60);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(201, 239);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.BackColor = System.Drawing.Color.Turquoise;
            this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(962, 334);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(201, 95);
            this.button2.TabIndex = 9;
            this.button2.Text = "This is my image!";
            this.button2.UseVisualStyleBackColor = false;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            this.button2.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(61, 4);
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(1013, 481);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(98, 21);
            this.checkBox1.TabIndex = 11;
            this.checkBox1.Text = "checkBox1";
            this.checkBox1.UseVisualStyleBackColor = true;
            this.checkBox1.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 16;
            this.listBox1.Location = new System.Drawing.Point(962, 517);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(201, 148);
            this.listBox1.TabIndex = 12;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.PaleTurquoise;
            this.ClientSize = new System.Drawing.Size(1208, 699);
            this.Controls.Add(this.MainPanel);
            this.Controls.Add(this.DetectedPanel);
            this.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.Name = "Form1";
            this.Text = "Generate Code With Images!";
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).EndInit();
            this.DetectedPanel.ResumeLayout(false);
            this.DetectedPanel.PerformLayout();
            this.MainPanel.ResumeLayout(false);
            this.MainPanel.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox ImagePictureBox;
        private System.Windows.Forms.Button LoadButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button RotateButton;
        private System.Windows.Forms.Panel DetectedPanel;
        private System.Windows.Forms.Button GenerateCodeButton;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.CheckedListBox DetectedBoxList;
        private System.Windows.Forms.Panel MainPanel;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.ListBox listBox1;
    }
}

