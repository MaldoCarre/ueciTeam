import "bootstrap/dist/css/bootstrap.min.css";
  // importando el js
import "bootstrap/dist/js/bootstrap.min.js";

//importando archivo popperjs . 
import "@popperjs/core"

import Navbar from './components/Navbar';
import Form from "./components/Form";

function App() {
    return (
      <div className="App">

        <Navbar>
        </Navbar>

        <Form></Form>



      </div>
    );
  }

export default App;
