import {useDropdownMenu} from "react-overlays";
import React from "react";

const MenuItem = ({ children, href }) => (
  <li>
    <a
      href={href}
      className="px-3 py-2 block hover:bg-gray-200"
    >
      {children}
    </a>
  </li>
);

const MenuList = () => {
  const { props } = useDropdownMenu();

  return (
    <ul
      role="menu"
      className="bg-white border rounded inline-block w-32 shadow"
      {...props}
    >
      <MenuItem href="#home">Home</MenuItem>
      <MenuItem href="#docs">Docs</MenuItem>
      <MenuItem href="#about">About</MenuItem>
    </ul>
  );
};


export default MenuList