package day04;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class MySwing06 extends JFrame {

   private JPanel contentPane;
   private JTextField textField;

   /**
    * Launch the application.
    */
   public static void main(String[] args) {
      EventQueue.invokeLater(new Runnable() {
         public void run() {
            try {
               MySwing06 frame = new MySwing06();
               frame.setVisible(true);
            } catch (Exception e) {
               e.printStackTrace();
            }
         }
      });
   }

   /**
    * Create the frame.
    */
   public MySwing06() {
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setBounds(100, 100, 450, 300);
      contentPane = new JPanel();
      contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
      setContentPane(contentPane);
      contentPane.setLayout(null);
      
      textField = new JTextField();
      textField.setBounds(12, 23, 154, 21);
      contentPane.add(textField);
      textField.setColumns(10);
      
      JButton btn1 = new JButton("1");
      btn1.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn1.getText();
         	 }else {
         		 tmp += btn1.getText();
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn1.setBounds(12, 54, 43, 23);
      contentPane.add(btn1);
      
      JButton btn_2 = new JButton("2");
      btn_2.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_2.getText();
         	 }else {
         		 tmp += btn_2.getText();
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_2.setBounds(67, 54, 43, 23);
      contentPane.add(btn_2);
      
      JButton btn_3 = new JButton("3");
      btn_3.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
        	 
        	 String tmp = textField.getText();
        	 
        	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
        		 tmp += "-";
        		 tmp += btn_3.getText();
        	 }else {
        		 tmp += btn_3.getText();
        	 }
        	 
        	 textField.setText( tmp );
        	 
         }
      });
      btn_3.setBounds(123, 54, 43, 23);
      contentPane.add(btn_3);
      
      JButton btn_4 = new JButton("4");
      btn_4.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_4.getText();
         	 }else {
         		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_4.getText();         			 
         		 }
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_4.setBounds(12, 87, 43, 23);
      contentPane.add(btn_4);
      
      JButton btn_5 = new JButton("5");
      btn_5.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_5.getText();
         	 }else {
         		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_5.getText();         			 
         		 }
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_5.setBounds(67, 87, 43, 23);
      contentPane.add(btn_5);
      
      JButton btn_6 = new JButton("6");
      btn_6.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
         }
      });
      btn_6.setBounds(123, 87, 43, 23);
      contentPane.add(btn_6);
      
      JButton btn_7 = new JButton("7");
      btn_7.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_7.getText();
         	 }else {
         		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_7.getText();         			 
         		 }
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_7.setBounds(12, 120, 43, 23);
      contentPane.add(btn_7);
      
      JButton btn_8 = new JButton("8");
      btn_8.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_8.getText();
         	 }else {
         		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_8.getText();         			 
         		 }
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_8.setBounds(67, 120, 43, 23);
      contentPane.add(btn_8);
      
      JButton btn_9 = new JButton("9");
      btn_9.addActionListener( new ActionListener() {
    	  public void actionPerformed(ActionEvent e) {
         	 
         	 String tmp = textField.getText();
         	 
         	 if( (tmp.length() == 3 || tmp.length() == 8 ) && tmp.length() <= 13 ) {
         		 tmp += "-";
         		 tmp += btn_9.getText();
         	 }else {
         		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_9.getText();         			 
         		 }
         	 }
         	 
         	 textField.setText( tmp );
          }
      });
      btn_9.setBounds(123, 120, 43, 23);
      contentPane.add(btn_9);
      
      JButton btn_0 = new JButton("0");
      btn_0.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
        	 
        	 String tmp = textField.getText();
        	 
        	 if( tmp.length() == 3 || tmp.length() == 8 ) {
        		 tmp += "-";
        		 tmp += btn_0.getText();
        	 }else {
        		 if( tmp.length() >= 13 ) {
         			 tmp += "";
         		 }else {
         			 tmp += btn_0.getText();         			 
         		 }
        	 }
        	 
        	 textField.setText( tmp );
         }
      });
      btn_0.setBounds(12, 153, 43, 23);
      contentPane.add(btn_0);
      
      //
      
      
      JButton btn_call = new JButton("call");
      btn_call.addActionListener(new ActionListener() {
          public void actionPerformed(ActionEvent e) {
        	  JOptionPane.showMessageDialog(null, "아이콘 없는 메시지 내용", "아이콘 없는 메시지 제목", JOptionPane.PLAIN_MESSAGE);
          }
       });
      btn_call.setBounds(67, 153, 99, 23);
      contentPane.add(btn_call);
   }

}