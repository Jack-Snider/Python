package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
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
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 270, 305);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("입력숫자 : ");
		lbl.setBounds(26, 33, 70, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(108, 30, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(26, 69, 198, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(26, 102, 198, 149);
		contentPane.add(ta);
	}

	
	public void myClick() {
		
		
		String answer = "";
		for( int i = 0; i < 3; i++ ) {
			answer += ( int )( Math.random() * 10 ) + 1;
		}
		
		
		String user = tf.getText();
		
		int strike = 0;
		int ball = 0;
		int out = 0;
		
		for( int i = 0; i < answer.length(); i++ ) {
			for( int j = 0; j < user.length(); j++ ) {
				
				if( user.charAt( i ) == answer.charAt( i ) ) {
					// 자리랑 숫자랑 같으면
					strike += 1;
					break;
				}else if( user.charAt( i ) == answer.charAt( j ) ) {
					// 자리는 같지 않지만 숫자가 같으면
					ball += 1;
					break;
				}else {
					// 아무것도 같은게 없으면
					out += 1;
					break;
				}
			}
		}
		
		
		ta.setText( "정답 : " + answer + "\n" + 
					strike + "S " + ball + "B " + out + "O"
					);
		
	}
	
}
