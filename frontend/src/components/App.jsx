import '../styles/App.css';
import Header from './Header';
import AllClimbs from './AllClimbs';
import Nav from './Nav';

export default function App() {


  return (
    <div className='app-wrapper'>
      <Header/>
      <Nav/>
      <AllClimbs/>
    </div>
  )
}
