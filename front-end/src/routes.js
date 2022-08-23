import Shipments from './components/Shipments'
import Home from './components/Home'

const routes = [
    { 
        path: '/',
        name: 'home',
        component: Home 
    },
    { 
        path: '/shipments',
        name: 'shipments',
        component: Shipments 
    },
]


export default routes