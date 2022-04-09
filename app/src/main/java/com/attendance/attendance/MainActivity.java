package com.attendance.attendance;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    TextView text;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text=findViewById(R.id.test1);
        if (!Python.isStarted()){
            Python.start(new AndroidPlatform(MainActivity.this));
        }
        PyObject py = Python.getInstance().getModule("Client");
        PyObject classobj = py.callAttr("main");
        text.setText(classobj.toString());

    }
}