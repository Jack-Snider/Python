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

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_second;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		
		
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 266, 316);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수 :");
		lbl_first.setBounds(35, 28, 57, 15);
		contentPane.add(lbl_first);
		
		tf_first = new JTextField();
		tf_first.setBounds(118, 25, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		JLabel lbl_second = new JLabel("끝별수 : ");
		lbl_second.setBounds(35, 68, 57, 15);
		contentPane.add(lbl_second);
		
		tf_second = new JTextField();
		tf_second.setBounds(118, 65, 116, 21);
		contentPane.add(tf_second);
		tf_second.setColumns(10);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(24, 144, 195, 103);
		contentPane.add(ta);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int start = Integer.parseInt( tf_first.getText() );
				int end = Integer.parseInt( tf_second.getText() );
				
				String str = "";
				
				for( int i = start; i <= end; i++ ) {
					for( int j = 1; j <= i; j++ ) {
						str += "*";
					}
					str += "\n";
				}
				
				ta.setText( str );
				
			}
		});
		btn.setBounds(79, 111, 97, 23);
		contentPane.add(btn);
		
		
	}
}
