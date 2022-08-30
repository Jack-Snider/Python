package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel tfb;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		tfb = new JPanel();
		tfb.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(tfb);
		tfb.setLayout(null);
		
		JTextArea tfa = new JTextArea();
		tfa.setBounds(12, 48, 78, 22);
		tfb.add(tfa);
		
		JTextArea textArea_1 = new JTextArea();
		textArea_1.setBounds(161, 48, 84, 22);
		tfb.add(textArea_1);
		
		JTextArea tfc = new JTextArea();
		tfc.setBounds(302, 48, 84, 22);
		tfb.add(tfc);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(111, 53, 38, 15);
		tfb.add(lblNewLabel);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int a = Integer.valueOf( tfa.getText() );
				int b = Integer.valueOf( textArea_1.getText() );
				
				int result = a + b;
				
				tfc.setText( result + "" );
				
				tfa.setText( "" );
				textArea_1.setText( "" );
				
				
				
			}
		});
		btn.setBounds(245, 49, 59, 23);
		tfb.add(btn);
	}
}
