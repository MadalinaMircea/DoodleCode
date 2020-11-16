
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.ImagePictureBox = new System.Windows.Forms.PictureBox();
            this.LoadButton = new System.Windows.Forms.Button();
            this.ParamBox = new System.Windows.Forms.RichTextBox();
            this.GenerateButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.FileBox = new System.Windows.Forms.TextBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.RotateButton = new System.Windows.Forms.Button();
            this.CropPictureBox = new System.Windows.Forms.PictureBox();
            this.PlusButton = new System.Windows.Forms.Button();
            this.MinusButton = new System.Windows.Forms.Button();
            this.CropButton = new System.Windows.Forms.Button();
            this.ResponseLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.CropPictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // ImagePictureBox
            // 
            this.ImagePictureBox.BackColor = System.Drawing.Color.MistyRose;
            this.ImagePictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.ImagePictureBox.Location = new System.Drawing.Point(12, 57);
            this.ImagePictureBox.Name = "ImagePictureBox";
            this.ImagePictureBox.Size = new System.Drawing.Size(305, 305);
            this.ImagePictureBox.TabIndex = 0;
            this.ImagePictureBox.TabStop = false;
            // 
            // LoadButton
            // 
            this.LoadButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadButton.Location = new System.Drawing.Point(12, 367);
            this.LoadButton.Name = "LoadButton";
            this.LoadButton.Size = new System.Drawing.Size(194, 54);
            this.LoadButton.TabIndex = 1;
            this.LoadButton.Text = "Load Picture";
            this.LoadButton.UseVisualStyleBackColor = true;
            this.LoadButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // ParamBox
            // 
            this.ParamBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ParamBox.Location = new System.Drawing.Point(540, 57);
            this.ParamBox.Name = "ParamBox";
            this.ParamBox.Size = new System.Drawing.Size(334, 239);
            this.ParamBox.TabIndex = 2;
            this.ParamBox.Text = "";
            // 
            // GenerateButton
            // 
            this.GenerateButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GenerateButton.Location = new System.Drawing.Point(597, 367);
            this.GenerateButton.Name = "GenerateButton";
            this.GenerateButton.Size = new System.Drawing.Size(242, 54);
            this.GenerateButton.TabIndex = 3;
            this.GenerateButton.Text = "Generate Code";
            this.GenerateButton.UseVisualStyleBackColor = true;
            this.GenerateButton.Click += new System.EventHandler(this.GenerateButton_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 25);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(95, 29);
            this.label1.TabIndex = 4;
            this.label1.Text = "Picture";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(535, 25);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(317, 29);
            this.label2.TabIndex = 5;
            this.label2.Text = "Parameters and Functions";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(535, 299);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(250, 29);
            this.label3.TabIndex = 6;
            this.label3.Text = "Output Folder Name";
            // 
            // FileBox
            // 
            this.FileBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FileBox.Location = new System.Drawing.Point(540, 331);
            this.FileBox.Name = "FileBox";
            this.FileBox.Size = new System.Drawing.Size(334, 30);
            this.FileBox.TabIndex = 7;
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
            this.RotateButton.Location = new System.Drawing.Point(212, 367);
            this.RotateButton.Name = "RotateButton";
            this.RotateButton.Size = new System.Drawing.Size(60, 54);
            this.RotateButton.TabIndex = 8;
            this.RotateButton.UseVisualStyleBackColor = true;
            this.RotateButton.Click += new System.EventHandler(this.button3_Click);
            // 
            // CropPictureBox
            // 
            this.CropPictureBox.BackColor = System.Drawing.SystemColors.Control;
            this.CropPictureBox.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("CropPictureBox.BackgroundImage")));
            this.CropPictureBox.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.CropPictureBox.Location = new System.Drawing.Point(228, 155);
            this.CropPictureBox.Name = "CropPictureBox";
            this.CropPictureBox.Size = new System.Drawing.Size(84, 84);
            this.CropPictureBox.TabIndex = 9;
            this.CropPictureBox.TabStop = false;
            this.CropPictureBox.Visible = false;
            this.CropPictureBox.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox2_MouseDown);
            this.CropPictureBox.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox2_MouseMove);
            this.CropPictureBox.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox2_MouseUp);
            // 
            // PlusButton
            // 
            this.PlusButton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("PlusButton.BackgroundImage")));
            this.PlusButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.PlusButton.Enabled = false;
            this.PlusButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PlusButton.Location = new System.Drawing.Point(278, 367);
            this.PlusButton.Name = "PlusButton";
            this.PlusButton.Size = new System.Drawing.Size(60, 54);
            this.PlusButton.TabIndex = 10;
            this.PlusButton.UseVisualStyleBackColor = true;
            this.PlusButton.Click += new System.EventHandler(this.button4_Click);
            // 
            // MinusButton
            // 
            this.MinusButton.BackColor = System.Drawing.SystemColors.Window;
            this.MinusButton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("MinusButton.BackgroundImage")));
            this.MinusButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.MinusButton.Enabled = false;
            this.MinusButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.MinusButton.Location = new System.Drawing.Point(344, 367);
            this.MinusButton.Name = "MinusButton";
            this.MinusButton.Size = new System.Drawing.Size(60, 54);
            this.MinusButton.TabIndex = 11;
            this.MinusButton.UseVisualStyleBackColor = false;
            this.MinusButton.Click += new System.EventHandler(this.button5_Click);
            // 
            // CropButton
            // 
            this.CropButton.Enabled = false;
            this.CropButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CropButton.Location = new System.Drawing.Point(410, 367);
            this.CropButton.Name = "CropButton";
            this.CropButton.Size = new System.Drawing.Size(113, 54);
            this.CropButton.TabIndex = 12;
            this.CropButton.Text = "Crop";
            this.CropButton.UseVisualStyleBackColor = true;
            this.CropButton.Click += new System.EventHandler(this.button6_Click);
            // 
            // ResponseLabel
            // 
            this.ResponseLabel.AutoSize = true;
            this.ResponseLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ResponseLabel.Location = new System.Drawing.Point(12, 459);
            this.ResponseLabel.Name = "ResponseLabel";
            this.ResponseLabel.Size = new System.Drawing.Size(131, 29);
            this.ResponseLabel.TabIndex = 13;
            this.ResponseLabel.Text = "Response";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(886, 497);
            this.Controls.Add(this.ResponseLabel);
            this.Controls.Add(this.CropButton);
            this.Controls.Add(this.MinusButton);
            this.Controls.Add(this.PlusButton);
            this.Controls.Add(this.CropPictureBox);
            this.Controls.Add(this.RotateButton);
            this.Controls.Add(this.FileBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.GenerateButton);
            this.Controls.Add(this.ParamBox);
            this.Controls.Add(this.LoadButton);
            this.Controls.Add(this.ImagePictureBox);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.CropPictureBox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox ImagePictureBox;
        private System.Windows.Forms.Button LoadButton;
        private System.Windows.Forms.RichTextBox ParamBox;
        private System.Windows.Forms.Button GenerateButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox FileBox;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button RotateButton;
        private System.Windows.Forms.PictureBox CropPictureBox;
        private System.Windows.Forms.Button PlusButton;
        private System.Windows.Forms.Button MinusButton;
        private System.Windows.Forms.Button CropButton;
        private System.Windows.Forms.Label ResponseLabel;
    }
}

