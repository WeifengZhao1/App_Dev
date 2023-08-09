/* eslint-disable jsx-a11y/alt-text */
import React from 'react';
import ReactDOM from 'react-dom/client';
import nightview from './images/nightview.jpg'
// --- FUNCTION COMPONENT ---
// content in the app
const App = function(){
    // create a constant variable
    const divText = 'I am a text in a variable'
    // create a style variable
    const styleJSX = {color:'purple',fontFamily:'Algerian'}

    return (
        <div>
            <h1 style={{color:"magenta",textAlign:"center"}}>Welcome to ReactJS</h1>
            <p>Let's familiar with JSX elements</p>

            <h2>Activity: bucket list</h2>
            <p>Proof of list</p>
            <ol>
                <li>It's a measureable form of progess</li>
                <li>It gives you things to look forward to</li>
                <li>It makes life more meaningful</li>
                <li>It helps you avoid languishing</li>
            </ol>

            <h2>Inline styling</h2>
            <label for="email" style={{color:"olive",padding:"0.5em 1em",fontWeight:'bolder'}}>Enter e-mail</label>
            <input id="email" type='text' placeholder='Type your email' style={{backgroundColor:'rgb(230,230,230',padding:'0.5em',borderRadius:'1em'}}></input>
            <button style={{marginLeft:'1em', backgroundColor:'magenta',padding:'0.5em 1em', borderRadius:'0.5em',color:'whitesmoke'}}>Submit form</button>
            <figure>
                <img src={nightview} style={{width:'50%', height:'500px'}}/>
            </figure>
            <p className='title'>Adding a class name to a JSX element</p>
            <p class='txtVar'>{divText}</p>
            <p style={styleJSX}>{divText}</p>
            <h2>Class activity</h2>
            <p> image with at least two inline styles</p>
            <img src={nightview} alt="nightview" style={{ width: '50%',height:'500px'}} />
            <img src={nightview} alt="nightview" style={{ width: '50%',height:'500px'}} />
        </div>
    )
}

//rooting the app
const root = ReactDOM.createRoot(document.querySelector('#root'))
root.render(App())