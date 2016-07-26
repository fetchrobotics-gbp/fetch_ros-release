Name:           ros-indigo-fetch-moveit-config
Version:        0.7.9
Release:        0%{?dist}
Summary:        ROS fetch_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-fetch-description
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-fake-controller-manager
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-python
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-moveit-simple-controller-manager
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rospy
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-fetch-description
BuildRequires:  ros-indigo-rostest

%description
An automatically generated package with all the configuration and launch files
for using the fetch_urdf with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 26 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.9-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.8-0
- Autogenerated by Bloom

* Mon Jun 20 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.7-0
- Autogenerated by Bloom

* Thu May 26 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.6-0
- Autogenerated by Bloom

* Sun May 08 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.5-0
- Autogenerated by Bloom

* Wed Mar 16 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.4-0
- Autogenerated by Bloom

* Sat Mar 05 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.3-0
- Autogenerated by Bloom

* Wed Feb 24 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.2-0
- Autogenerated by Bloom

* Wed Jan 20 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.1-0
- Autogenerated by Bloom

* Tue Sep 29 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.0-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Jul 03 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.0-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.14-0
- Autogenerated by Bloom

* Sat Jun 13 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.13-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.12-0
- Autogenerated by Bloom

* Wed Jun 10 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.11-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.10-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.9-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.8-0
- Autogenerated by Bloom

* Fri Jun 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.7-0
- Autogenerated by Bloom

* Thu Jun 04 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.6-0
- Autogenerated by Bloom

* Wed Jun 03 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.5-0
- Autogenerated by Bloom

* Sun May 31 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.4-1
- Autogenerated by Bloom

