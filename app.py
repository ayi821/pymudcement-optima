"""
PyMudCement-Optima Main Application
Complete Drilling Engineering Software with Mud Formulation
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Configure the page
st.set_page_config(
    page_title="PyMudCement-Optima",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== TITLE ==========
st.title("🛢️ PyMudCement-Optima")
st.markdown("### Intelligent Mud & Cement Design Suite")
st.markdown("---")

# ========== SIDEBAR NAVIGATION ==========
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Module",
    ["🏠 Dashboard", 
     "💧 Drilling Fluids", 
     "🧪 Mud Formulation",
     "🔬 Rheology Analysis",
     "🧱 Cementing Design",
     "🔌 Plug & Abandonment",
     "📊 Pressure Profile"]
)

# ============================================
# PAGE 1: DASHBOARD
# ============================================
if page == "🏠 Dashboard":
    st.header("📊 Dashboard")
    
    st.info("""
    Welcome to PyMudCement-Optima!
    
    This software helps you design drilling mud and cement for oil wells.
    
    **How to use:**
    1. Go to "Drilling Fluids" to enter mud properties
    2. Go to "Mud Formulation" to select the right mud for your rock type
    3. Check rheology in "Rheology Analysis"
    4. Design cement in "Cementing Design"
    5. Design plugs in "Plug & Abandonment"
    6. Check safety in "Pressure Profile"
    """)
    
    # Status indicators
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        if 'mud_properties' in st.session_state:
            st.metric("Mud Properties", "✅ Set", delta="Ready")
        else:
            st.metric("Mud Properties", "❌ Not Set", delta="Go to Fluids")
    
    with col2:
        if 'formulation_done' in st.session_state:
            st.metric("Mud Formulation", "✅ Done", delta="Ready")
        else:
            st.metric("Mud Formulation", "❌ Not Done", delta="Formulate")
    
    with col3:
        if 'rheology_checked' in st.session_state:
            st.metric("Rheology", "✅ Checked", delta="OK")
        else:
            st.metric("Rheology", "❌ Not Checked", delta="Check")
    
    with col4:
        if 'cement_designed' in st.session_state:
            st.metric("Cement Design", "✅ Complete", delta="Ready")
        else:
            st.metric("Cement Design", "❌ Not Done", delta="Design")
    
    with col5:
        if 'plug_designed' in st.session_state:
            st.metric("Plug Design", "✅ Complete", delta="Ready")
        else:
            st.metric("Plug Design", "❌ Not Done", delta="Design")
    
    with col6:
        if 'pressure_checked' in st.session_state:
            st.metric("Pressure Profile", "✅ Checked", delta="OK")
        else:
            st.metric("Pressure Profile", "❌ Not Checked", delta="Check")


# ============================================
# PAGE 2: DRILLING FLUIDS
# ============================================
elif page == "💧 Drilling Fluids":
    st.header("💧 Drilling Fluids Engineering")
    st.markdown("Enter your drilling mud properties below:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mud_weight = st.number_input(
            "Mud Weight (kg/m³)",
            min_value=800.0,
            max_value=3000.0,
            value=1200.0,
            step=10.0,
            help="Typical: 1000-2000 kg/m³"
        )
        
        plastic_viscosity = st.number_input(
            "Plastic Viscosity (cP)",
            min_value=0.0,
            max_value=100.0,
            value=15.0,
            step=0.5,
            help="Typical: 5-50 cP"
        )
    
    with col2:
        yield_point = st.number_input(
            "Yield Point (lb/100ft²)",
            min_value=0.0,
            max_value=50.0,
            value=10.0,
            step=0.5,
            help="Typical: 5-30 lb/100ft²"
        )
        
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-10.0,
            max_value=300.0,
            value=25.0,
            step=1.0
        )
    
    if st.button("💾 Save Mud Properties", type="primary"):
        st.session_state.mud_properties = {
            'mud_weight': mud_weight,
            'plastic_viscosity': plastic_viscosity,
            'yield_point': yield_point,
            'temperature': temperature
        }
        st.success("✅ Mud properties saved successfully!")
        st.json(st.session_state.mud_properties)
    
    # Show current properties if they exist
    if 'mud_properties' in st.session_state:
        st.subheader("📋 Current Mud Properties")
        st.json(st.session_state.mud_properties)


# ============================================
# PAGE 3: MUD FORMULATION
# ============================================
elif page == "🧪 Mud Formulation":
    st.header("🧪 Drilling Mud Formulation")
    st.markdown("Select the right mud system based on reservoir rock compatibility")
    
    st.info("""
    **Why Mud Formulation Matters:**
    - Different rocks react differently with drilling fluids
    - Wrong mud can cause formation damage
    - Proper formulation improves drilling efficiency and well productivity
    """)
    
    # ---------- ROCK TYPE SELECTION ----------
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Reservoir Rock")
        
        rock_type = st.selectbox(
            "Select Rock Type",
            [
                "Sandstone (Quartz-rich)",
                "Carbonate (Limestone/Dolomite)",
                "Shale (Clay-rich)",
                "Salt Formation",
                "Reactive Clay (Smectite/Illite)",
                "Fractured Carbonate",
                "Tight Sandstone",
                "Chalk"
            ],
            help="Select the type of rock you'll be drilling through"
        )
        
        formation_temperature = st.number_input(
            "Formation Temperature (°C)",
            min_value=0,
            max_value=300,
            value=60,
            step=5,
            help="Expected temperature of the formation"
        )
        
        formation_pressure = st.number_input(
            "Formation Pressure (MPa)",
            min_value=0.0,
            max_value=100.0,
            value=25.0,
            step=0.5,
            help="Expected pressure of the formation"
        )
    
    with col2:
        st.subheader("Rock Properties")
        
        # Rock-specific properties
        if rock_type == "Sandstone (Quartz-rich)":
            st.info("""
            **Sandstone Properties:**
            - Highly permeable
            - Low reactivity
            - Moderate to high porosity
            - Common reservoir rock
            
            **Compatibility Notes:**
            - Most mud systems work well
            - Avoid excessive solids
            - Good filtration control needed
            """)
            recommended_muds = [
                "Water-Based Mud (WBM) - Standard",
                "Water-Based Mud (WBM) - Polymer",
                "Low Solids Mud",
                "Bentonite Mud"
            ]
            
        elif rock_type == "Carbonate (Limestone/Dolomite)":
            st.info("""
            **Carbonate Properties:**
            - Acid-soluble
            - May have fractures
            - Reactive with acids
            - Often vuggy
            
            **Compatibility Notes:**
            - Avoid acidic muds
            - Use calcium-tolerant fluids
            - Consider oil-based for fracturing
            """)
            recommended_muds = [
                "Water-Based Mud (WBM) - Polymer",
                "Oil-Based Mud (OBM)",
                "Synthetic-Based Mud (SBM)",
                "Calcium-Tolerant WBM"
            ]
            
        elif rock_type == "Shale (Clay-rich)":
            st.info("""
            **Shale Properties:**
            - Highly reactive
            - Swells in water
            - Low permeability
            - High clay content
            
            **Compatibility Notes:**
            - Use inhibitive muds
            - High salinity recommended
            - Oil-based preferred
            """)
            recommended_muds = [
                "Oil-Based Mud (OBM)",
                "Synthetic-Based Mud (SBM)",
                "High-Salinity WBM",
                "Potassium-Based WBM"
            ]
            
        elif rock_type == "Salt Formation":
            st.info("""
            **Salt Properties:**
            - Highly soluble
            - Plastic behavior
            - Reactive with water
            - Can cause wellbore instability
            
            **Compatibility Notes:**
            - Use salt-saturated muds
            - Oil-based preferred
            - Avoid freshwater muds
            """)
            recommended_muds = [
                "Salt-Saturated WBM",
                "Oil-Based Mud (OBM)",
                "Synthetic-Based Mud (SBM)",
                "Glycol-Based Mud"
            ]
            
        elif rock_type == "Reactive Clay (Smectite/Illite)":
            st.info("""
            **Reactive Clay Properties:**
            - Swells significantly
            - Disperse in water
            - Highly reactive
            - Causes wellbore problems
            
            **Compatibility Notes:**
            - Use highly inhibitive muds
            - Oil-based strongly recommended
            - High KCL content beneficial
            """)
            recommended_muds = [
                "Oil-Based Mud (OBM)",
                "Synthetic-Based Mud (SBM)",
                "KCL-Polymer WBM",
                "PHPA-Polymer WBM"
            ]
            
        elif rock_type == "Fractured Carbonate":
            st.info("""
            **Fractured Carbonate Properties:**
            - Natural fractures
            - Loss circulation risk
            - Acid-reactive
            - Often productive zones
            
            **Compatibility Notes:**
            - Use bridging agents
            - Low fluid loss needed
            - Consider reactive fluids
            """)
            recommended_muds = [
                "Water-Based Mud (WBM) - Bridging",
                "Oil-Based Mud (OBM)",
                "Lost Circulation Materials (LCM)",
                "Acid-Soluble WBM"
            ]
            
        elif rock_type == "Tight Sandstone":
            st.info("""
            **Tight Sandstone Properties:**
            - Low permeability
            - High capillary pressure
            - Deep formation
            - Hard and abrasive
            
            **Compatibility Notes:**
            - Low solids required
            - Excellent filtration control
            - Lubricity important
            """)
            recommended_muds = [
                "Oil-Based Mud (OBM)",
                "Synthetic-Based Mud (SBM)",
                "Low Solids Polymer WBM",
                "Water-Based Mud (WBM)"
            ]
            
        else:  # Chalk
            st.info("""
            **Chalk Properties:**
            - Soft, porous
            - Low strength
            - Acid-reactive
            - Often fractured
            
            **Compatibility Notes:**
            - Avoid high shear
            - Use low-density fluids
            - Consider calcium-based
            """)
            recommended_muds = [
                "Water-Based Mud (WBM)",
                "Calcium Carbonate WBM",
                "Oil-Based Mud (OBM)",
                "Low Density Mud"
            ]
    
    # ---------- SELECT MUD SYSTEM ----------
    st.markdown("---")
    st.subheader("🛢️ Recommended Mud Systems")
    
    st.info(f"**Based on {rock_type}, these mud systems are recommended:**")
    
    for i, mud in enumerate(recommended_muds, 1):
        st.write(f"{i}. {mud}")
    
    # ---------- DETAILED FORMULATION ----------
    st.markdown("---")
    st.subheader("📋 Detailed Mud Formulation")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        selected_mud = st.selectbox(
            "Select Mud System to Formulate",
            recommended_muds,
            help="Choose the mud system you want to formulate"
        )
    
    with col2:
        desired_density = st.number_input(
            "Target Mud Density (kg/m³)",
            min_value=800,
            max_value=2500,
            value=1200,
            step=10,
            help="Desired mud weight"
        )
    
    if st.button("🧪 Generate Formulation", type="primary"):
        try:
            st.markdown("---")
            st.subheader(f"📊 {selected_mud} Formulation")
            
            # ---------- FORMULATION DETAILS ----------
            if "Water-Based" in selected_mud:
                st.info("**Base Fluid:** Fresh Water or Salt Water")
                
                if "Bentonite" in selected_mud:
                    components = {
                        "Water": "1000 L",
                        "Bentonite": f"{20 + (desired_density - 1000) / 10:.1f} kg",
                        "Caustic Soda (pH control)": "0.5 kg",
                        "Soda Ash": "0.5 kg",
                        "Barite (weighting)": f"{max(0, (desired_density - 1000) * 1.5):.1f} kg",
                        "CMC (filtration control)": "1.0 kg"
                    }
                    
                elif "Polymer" in selected_mud:
                    components = {
                        "Water": "1000 L",
                        "Polymer (PHPA)": "0.5 kg",
                        "Xanthan Gum (viscosity)": "0.3 kg",
                        "Starch (filtration)": "2.0 kg",
                        "Barite (weighting)": f"{max(0, (desired_density - 1000) * 1.5):.1f} kg",
                        "KCl (inhibition)": "5.0 kg",
                        "Caustic Soda": "0.3 kg"
                    }
                    
                elif "Salt-Saturated" in selected_mud:
                    components = {
                        "Saturated Salt Water": "1000 L",
                        "Bentonite (pre-hydrated)": "10.0 kg",
                        "Starch (filtration)": "3.0 kg",
                        "CMC (viscosity)": "1.5 kg",
                        "Barite": f"{max(0, (desired_density - 1200) * 1.5):.1f} kg",
                        "Salt (maintenance)": "300.0 kg"
                    }
                    
                elif "KCL-Polymer" in selected_mud:
                    components = {
                        "Water": "1000 L",
                        "KCl": "50.0 kg",
                        "Polymer (PHPA)": "0.8 kg",
                        "Xanthan Gum": "0.4 kg",
                        "Starch": "2.5 kg",
                        "Barite": f"{max(0, (desired_density - 1100) * 1.5):.1f} kg",
                        "Caustic Soda": "0.4 kg"
                    }
                    
                elif "Bridging" in selected_mud:
                    components = {
                        "Water": "1000 L",
                        "Bentonite": "25.0 kg",
                        "Calcium Carbonate (bridging)": "50.0 kg",
                        "Polymer (viscosity)": "0.5 kg",
                        "Barite": f"{max(0, (desired_density - 1100) * 1.5):.1f} kg",
                        "Lost Circulation Material": "20.0 kg",
                        "Caustic Soda": "0.5 kg"
                    }
                    
                else:
                    components = {
                        "Water": "1000 L",
                        "Bentonite": "25.0 kg",
                        "Barite": f"{max(0, (desired_density - 1000) * 1.5):.1f} kg",
                        "CMC (filtration)": "1.5 kg",
                        "Caustic Soda": "0.5 kg"
                    }
                    
            elif "Oil-Based" in selected_mud or "Synthetic" in selected_mud:
                st.info("**Base Fluid:** Diesel Oil or Synthetic Fluid")
                
                if "Oil-Based Mud (OBM)" in selected_mud:
                    components = {
                        "Diesel Oil/Synthetic": "800 L",
                        "Water (emulsified)": "200 L",
                        "Emulsifier": "15.0 L",
                        "Organophilic Clay": "10.0 kg",
                        "Barite": f"{max(0, (desired_density - 900) * 1.8):.1f} kg",
                        "Lime": "2.5 kg",
                        "Calcium Chloride": "5.0 kg"
                    }
                else:
                    components = {
                        "Synthetic Fluid": "850 L",
                        "Water (emulsified)": "150 L",
                        "Emulsifier": "12.0 L",
                        "Organophilic Clay": "8.0 kg",
                        "Barite": f"{max(0, (desired_density - 900) * 1.8):.1f} kg",
                        "Lime": "2.0 kg"
                    }
                    
            elif "Calcium-Tolerant" in selected_mud:
                components = {
                    "Water": "1000 L",
                    "Bentonite": "15.0 kg",
                    "Calcium-Tolerant Polymer": "0.5 kg",
                    "Starch": "2.0 kg",
                    "Barite": f"{max(0, (desired_density - 1000) * 1.5):.1f} kg",
                    "Caustic Soda": "0.3 kg"
                }
                
            else:
                components = {
                    "Water": "1000 L",
                    "Bentonite": "25.0 kg",
                    "Barite": f"{max(0, (desired_density - 1000) * 1.5):.1f} kg",
                    "CMC": "1.5 kg"
                }
            
            # ---------- DISPLAY FORMULATION ----------
            st.markdown("**Per 1000 Liters of Mud:**")
            
            comp_df = pd.DataFrame({
                'Component': list(components.keys()),
                'Quantity': list(components.values())
            })
            st.dataframe(comp_df, use_container_width=True)
            
            # ---------- PROPERTIES ----------
            st.markdown("---")
            st.subheader("📊 Estimated Mud Properties")
            
            if "Water-Based" in selected_mud:
                base_density = 1000
                base_viscosity = 15
                base_yp = 8
                base_ph = 10.5
                base_filtration = 8
            elif "Oil-Based" in selected_mud:
                base_density = 900
                base_viscosity = 20
                base_yp = 12
                base_ph = 10.0
                base_filtration = 3
            else:
                base_density = 1000
                base_viscosity = 15
                base_yp = 10
                base_ph = 10.5
                base_filtration = 6
            
            density_adjustment = (desired_density - base_density) / 50
            final_density = desired_density
            final_viscosity = base_viscosity + density_adjustment * 2
            final_yp = base_yp + density_adjustment * 1.5
            final_ph = base_ph
            final_filtration = base_filtration - density_adjustment * 0.1
            
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Density", f"{final_density:.0f} kg/m³")
            with col2:
                st.metric("Viscosity (PV)", f"{final_viscosity:.1f} cP")
            with col3:
                st.metric("Yield Point (YP)", f"{final_yp:.1f} lb/100ft²")
            with col4:
                st.metric("pH", f"{final_ph:.1f}")
            with col5:
                st.metric("Filtration (API)", f"{final_filtration:.1f} mL/30min")
            
            # ---------- COMPATIBILITY CHECK ----------
            st.markdown("---")
            st.subheader("✅ Rock-Fluid Compatibility Check")
            
            compatibility_score = 0
            checks = []
            
            if "Water-Based" in selected_mud:
                if rock_type in ["Shale (Clay-rich)", "Reactive Clay (Smectite/Illite)"]:
                    checks.append(("Water-based with reactive clay", "⚠️", "Potential swelling issues"))
                    compatibility_score -= 2
                elif rock_type in ["Salt Formation"]:
                    checks.append(("Water-based with salt", "⚠️", "Salt dissolution risk"))
                    compatibility_score -= 1
                else:
                    checks.append(("Water-based with rock type", "✅", "Compatible"))
                    compatibility_score += 2
                    
            elif "Oil-Based" in selected_mud or "Synthetic" in selected_mud:
                if rock_type in ["Shale (Clay-rich)", "Reactive Clay (Smectite/Illite)", "Salt Formation"]:
                    checks.append(("Oil-based with reactive formation", "✅", "Highly compatible"))
                    compatibility_score += 3
                else:
                    checks.append(("Oil-based with rock type", "✅", "Compatible"))
                    compatibility_score += 2
            
            if formation_temperature > 120:
                if "Polymer" in selected_mud and "Water-Based" in selected_mud:
                    checks.append(("High temperature with polymer", "⚠️", "Polymer degradation risk"))
                    compatibility_score -= 1
                else:
                    checks.append(("High temperature", "✅", "Mud is thermally stable"))
                    compatibility_score += 1
            else:
                checks.append(("Temperature", "✅", "Well within range"))
                compatibility_score += 1
            
            if desired_density < 1000:
                checks.append(("Low density", "⚠️", "May not provide enough hydrostatic pressure"))
                compatibility_score -= 1
            elif desired_density > 2000:
                checks.append(("High density", "⚠️", "May cause lost circulation"))
                compatibility_score -= 1
            else:
                checks.append(("Density", "✅", "Within safe range"))
                compatibility_score += 1
            
            for check in checks:
                if "✅" in check[1]:
                    st.success(f"{check[0]}: {check[1]} {check[2]}")
                elif "⚠️" in check[1]:
                    st.warning(f"{check[0]}: {check[1]} {check[2]}")
                else:
                    st.info(f"{check[0]}: {check[1]} {check[2]}")
            
            st.markdown("---")
            if compatibility_score >= 5:
                st.success("""
                🟢 **EXCELLENT COMPATIBILITY**
                This mud system is highly compatible with the formation.
                """)
            elif compatibility_score >= 3:
                st.info("""
                🟡 **GOOD COMPATIBILITY**
                This mud system is compatible but may need minor adjustments.
                """)
            else:
                st.warning("""
                🔶 **CONSIDER ALTERNATIVE MUD SYSTEM**
                This combination may cause formation damage or wellbore instability.
                Consider an alternative mud system.
                """)
            
            # ---------- RECOMMENDATIONS ----------
            st.markdown("---")
            st.subheader("💡 Recommendations")
            
            if "Water-Based" in selected_mud and "Shale" in rock_type:
                st.info("📌 Consider switching to Oil-Based Mud for better shale inhibition")
            
            if "Salt" in rock_type and "Water-Based" in selected_mud:
                st.info("📌 Ensure salt-saturated system to prevent salt dissolution")
            
            if formation_temperature > 120 and "Water-Based" in selected_mud:
                st.info("📌 Use temperature-stable polymers for high-temperature wells")
            
            if desired_density > 1900:
                st.info("📌 High-density mud requires careful solids control and weighting agents")
            
            st.success("✅ Mud formulation generated successfully!")
            st.session_state.formulation_done = True
            
        except Exception as e:
            st.error(f"❌ Error generating formulation: {str(e)}")


# ============================================
# PAGE 4: RHEOLOGY ANALYSIS
# ============================================
elif page == "🔬 Rheology Analysis":
    st.header("🔬 Rheology Analysis")
    
    if 'mud_properties' not in st.session_state:
        st.warning("⚠️ Please enter mud properties in 'Drilling Fluids' first!")
        st.stop()
    
    mud = st.session_state.mud_properties
    
    # Display current properties
    st.subheader("📋 Current Mud Properties")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Mud Weight", f"{mud['mud_weight']} kg/m³")
    with col2:
        st.metric("PV", f"{mud['plastic_viscosity']} cP")
    with col3:
        st.metric("YP", f"{mud['yield_point']} lb/100ft²")
    with col4:
        st.metric("Temperature", f"{mud['temperature']} °C")
    
    # Import and use rheology module
    try:
        from src.fluids.rheology import BinghamPlasticModel
        
        # Convert units
        pv_pas = mud['plastic_viscosity'] / 1000
        yp_pa = mud['yield_point'] * 0.4788
        
        # Create model
        model = BinghamPlasticModel(pv_pas, yp_pa)
        
        # Calculate results
        shear_rates = np.linspace(0.1, 500, 50)
        shear_stresses = [model.shear_stress(gamma) for gamma in shear_rates]
        
        # Display table
        st.subheader("📊 Rheological Calculations")
        
        results_df = pd.DataFrame({
            'Shear Rate (s⁻¹)': shear_rates,
            'Shear Stress (Pa)': shear_stresses
        })
        st.dataframe(results_df, use_container_width=True)
        
        # Show formula
        st.markdown("""
        **Formula used:** τ = τ_y + μ_p × γ
        
        Where:
        - τ = Shear stress (Pa)
        - τ_y = Yield point (Pa)
        - μ_p = Plastic viscosity (Pa·s)
        - γ = Shear rate (s⁻¹)
        """)
        
        # Plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=shear_rates,
            y=shear_stresses,
            mode='lines',
            name='Shear Stress',
            line=dict(color='blue', width=3)
        ))
        fig.update_layout(
            title="Shear Stress vs Shear Rate",
            xaxis_title="Shear Rate (s⁻¹)",
            yaxis_title="Shear Stress (Pa)",
            hovermode='x'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.session_state.rheology_checked = True
        st.success("✅ Rheology analysis complete!")
        
    except Exception as e:
        st.error(f"Error in rheology calculation: {str(e)}")


# ============================================
# PAGE 5: CEMENTING DESIGN
# ============================================
elif page == "🧱 Cementing Design":
    st.header("🧱 Cementing Design")
    
    st.subheader("Well Conditions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        depth = st.number_input(
            "Casing Shoe Depth (m)",
            min_value=100.0,
            max_value=10000.0,
            value=2000.0,
            step=100.0,
            help="Total depth of the casing shoe"
        )
        
        temperature = st.number_input(
            "Bottom Hole Temperature (°C)",
            min_value=0.0,
            max_value=300.0,
            value=60.0,
            step=5.0,
            help="Temperature at the bottom of the well"
        )
    
    with col2:
        density_required = st.slider(
            "Required Slurry Density (kg/m³)",
            min_value=1500,
            max_value=2300,
            value=1890,
            step=10,
            help="Target density for the cement slurry"
        )
        
        cement_class = st.selectbox(
            "Cement Class",
            ["Class G", "Class H", "Class A", "Class B"],
            help="API cement classification"
        )
    
    # Hole geometry
    st.subheader("Hole Geometry")
    col1, col2 = st.columns(2)
    with col1:
        hole_diameter = st.number_input(
            "Hole Diameter (m)",
            min_value=0.1,
            max_value=1.0,
            value=0.311,
            step=0.001,
            format="%.3f",
            help="Open hole diameter"
        )
    with col2:
        casing_od = st.number_input(
            "Casing OD (m)",
            min_value=0.05,
            max_value=0.5,
            value=0.245,
            step=0.001,
            format="%.3f",
            help="Casing outer diameter"
        )
    
    # Excess factor
    excess_factor = st.slider(
        "Open Hole Excess Factor (W_e)",
        min_value=0.0,
        max_value=0.5,
        value=0.15,
        step=0.01,
        help="Accounts for washouts and irregularities"
    )
    
    # ---------- DESIGN SLURRY BUTTON ----------
    if st.button("🎯 Design Slurry", type="primary"):
        try:
            # Validate inputs
            if hole_diameter <= casing_od:
                st.error("❌ Hole diameter must be greater than casing OD!")
                st.stop()
            
            # Calculate water-cement ratio
            if cement_class == "Class G":
                water_cement_ratio = 0.44
            elif cement_class == "Class H":
                water_cement_ratio = 0.38
            else:
                water_cement_ratio = 0.50
            
            # Calculate volumes
            annular_volume = (np.pi / 4) * (hole_diameter**2 - casing_od**2) * depth
            annular_volume_with_excess = annular_volume * (1 + excess_factor)
            slurry_volume = annular_volume_with_excess * 1.05  # 5% safety margin
            
            # Save to session state
            st.session_state.cement_designed = True
            st.session_state.cement_design = {
                'class': cement_class,
                'density': density_required,
                'annular_volume': annular_volume,
                'slurry_volume': slurry_volume,
                'excess_factor': excess_factor,
                'water_cement_ratio': water_cement_ratio,
                'temperature': temperature,
                'depth': depth
            }
            
            # ---------- DISPLAY RESULTS ----------
            st.markdown("---")
            st.subheader("📊 Slurry Design Results")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cement Class", cement_class)
                st.metric("W/C Ratio", f"{water_cement_ratio:.2f}")
            with col2:
                st.metric("Slurry Density", f"{density_required} kg/m³")
                st.metric("Annular Volume", f"{annular_volume:.2f} m³")
            with col3:
                st.metric("Slurry Volume", f"{slurry_volume:.2f} m³")
                st.metric("Excess Factor", f"{excess_factor*100:.0f}%")
            
            # ---------- FEATURE 1: LEAD/TAIL SLURRY ----------
            st.markdown("---")
            st.subheader("📊 Slurry Breakdown")
            
            col1, col2 = st.columns(2)
            with col1:
                lead_percent = st.slider(
                    "Lead Slurry Percentage (%)",
                    min_value=0,
                    max_value=100,
                    value=60,
                    step=5,
                    help="Percentage of total slurry for lead"
                )
            with col2:
                tail_percent = 100 - lead_percent
                st.metric("Tail Slurry Percentage", f"{tail_percent}%")
            
            lead_volume = slurry_volume * (lead_percent / 100)
            tail_volume = slurry_volume * (tail_percent / 100)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Lead Slurry Volume", f"{lead_volume:.2f} m³")
                st.caption(f"{lead_percent}% of total")
            with col2:
                st.metric("Tail Slurry Volume", f"{tail_volume:.2f} m³")
                st.caption(f"{tail_percent}% of total")
            with col3:
                st.metric("Total Slurry", f"{slurry_volume:.2f} m³")
            
            # ---------- FEATURE 2: SPACER & WASH FLUIDS ----------
            st.markdown("---")
            st.subheader("🧪 Spacer & Wash Fluids")
            
            col1, col2 = st.columns(2)
            with col1:
                spacer_percent = st.slider(
                    "Spacer Fluid (% of annulus)",
                    min_value=0,
                    max_value=30,
                    value=10,
                    step=1,
                    help="Volume of spacer fluid as % of annulus"
                )
            with col2:
                wash_percent = st.slider(
                    "Wash/Flush Fluid (% of annulus)",
                    min_value=0,
                    max_value=20,
                    value=5,
                    step=1,
                    help="Volume of wash fluid as % of annulus"
                )
            
            spacer_volume = annular_volume * (spacer_percent / 100)
            wash_volume = annular_volume * (wash_percent / 100)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Spacer Volume", f"{spacer_volume:.2f} m³")
                st.caption(f"{spacer_percent}% of annulus")
            with col2:
                st.metric("Wash Volume", f"{wash_volume:.2f} m³")
                st.caption(f"{wash_percent}% of annulus")
            with col3:
                total_fluids = spacer_volume + wash_volume
                st.metric("Total Fluids", f"{total_fluids:.2f} m³")
            
            # ---------- FEATURE 3: ADDITIVE RECOMMENDATIONS ----------
            st.markdown("---")
            st.subheader("🔬 Additive Recommendations")
            
            bh_temp = st.number_input(
                "Bottom Hole Temperature for Additives (°C)",
                min_value=0.0,
                max_value=300.0,
                value=60.0,
                step=5.0,
                help="Temperature for additive selection"
            )
            
            if bh_temp > 120:
                st.warning("🔥 High Temperature Well")
                st.info("📌 Recommended: RETARDER (Lignosulfonate)")
                st.info("📌 Concentration: 0.2-0.6% BWOC")
                st.info("📌 Prevents flash setting in deep hot wells")
                pump_time_estimate = 120
            elif bh_temp > 80:
                st.info("🌡️ Moderate Temperature Well")
                st.info("📌 Recommended: DISPERSANT (Lignosulfonate)")
                st.info("📌 Concentration: 0.1-0.3% BWOC")
                st.info("📌 Improves flow properties")
                pump_time_estimate = 90
            elif bh_temp < 30:
                st.info("❄️ Low Temperature Well")
                st.info("📌 Recommended: ACCELERATOR (Calcium Chloride)")
                st.info("📌 Concentration: 0.5-2.0% BWOC")
                st.info("📌 Accelerates setting time")
                pump_time_estimate = 60
            else:
                st.success("✅ Normal Temperature Well")
                st.info("📌 Recommended: Standard cement mix")
                st.info("📌 No special additives required")
                pump_time_estimate = 100
            
            # Pump rate calculation
            pump_rate = st.number_input(
                "Pump Rate (m³/min)",
                min_value=0.1,
                max_value=5.0,
                value=0.5,
                step=0.1,
                help="Expected pumping rate"
            )
            
            actual_pump_time = slurry_volume / pump_rate
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Estimated Max Pump Time", f"{pump_time_estimate} minutes")
            with col2:
                st.metric("Required Pump Time", f"{actual_pump_time:.1f} minutes")
            
            if actual_pump_time > pump_time_estimate:
                st.error(f"❌ Required pump time ({actual_pump_time:.1f} min) exceeds max ({pump_time_estimate} min)!")
                st.warning("⚠️ Add more retarder or increase pumping rate!")
            else:
                st.success(f"✅ Pump time ({actual_pump_time:.1f} min) is within limits")
            
            # ---------- FEATURE 4: PLUG BUMPING PRESSURE ----------
            st.markdown("---")
            st.subheader("🔧 Plug Bumping Pressure")
            
            col1, col2 = st.columns(2)
            with col1:
                displacement_density = st.number_input(
                    "Displacement Fluid Density (kg/m³)",
                    min_value=800.0,
                    max_value=2500.0,
                    value=1200.0,
                    step=10.0,
                    help="Density of displacement fluid"
                )
            with col2:
                fracture_pressure = st.number_input(
                    "Formation Fracture Pressure (MPa)",
                    min_value=0.0,
                    max_value=100.0,
                    value=40.0,
                    step=0.5,
                    help="Maximum pressure the formation can handle"
                )
            
            gravity = 9.81
            hydrostatic_pressure = displacement_density * gravity * depth / 1e6
            bumping_pressure = hydrostatic_pressure * 1.1  # 10% overbalance
            max_safe_pressure = fracture_pressure * 0.95
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Hydrostatic Pressure", f"{hydrostatic_pressure:.2f} MPa")
            with col2:
                st.metric("Recommended Bumping", f"{bumping_pressure:.2f} MPa")
            with col3:
                st.metric("Maximum Safe", f"{max_safe_pressure:.2f} MPa")
            
            if bumping_pressure > max_safe_pressure:
                st.error(f"❌ BUMPING PRESSURE EXCEEDS SAFE LIMIT!")
                st.error(f"Bumping: {bumping_pressure:.2f} MPa > Maximum: {max_safe_pressure:.2f} MPa")
                st.warning("⚠️ Reduce displacement density or use lighter fluid!")
            else:
                st.success(f"✅ Safe bumping pressure: {bumping_pressure:.2f} MPa")
                st.info(f"Safety margin: {max_safe_pressure - bumping_pressure:.2f} MPa")
            
            st.success("✅ Cement design complete!")
            
        except Exception as e:
            st.error(f"❌ Error in cement design: {str(e)}")
            st.info("Please check your inputs and try again.")


# ============================================
# PAGE 6: PLUG & ABANDONMENT
# ============================================
elif page == "🔌 Plug & Abandonment":
    st.header("🔌 Plug & Abandonment Design")
    
    st.subheader("Plug Configuration")
    
    plug_type = st.selectbox(
        "Select Plug Type",
        ["Abandonment (P&A)", "Sidetrack", "Well Suspension"],
        help="Type of plug to design"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        hole_diameter_plug = st.number_input(
            "Hole Diameter (m)",
            min_value=0.1,
            max_value=1.0,
            value=0.311,
            step=0.001,
            format="%.3f",
            help="Open hole diameter"
        )
        
        plug_top_depth = st.number_input(
            "Plug Top Depth (m)",
            min_value=0.0,
            max_value=10000.0,
            value=500.0,
            step=50.0,
            help="Top of cement plug"
        )
    
    with col2:
        plug_density = st.number_input(
            "Slurry Density (kg/m³)",
            min_value=1500,
            max_value=2300,
            value=1900,
            step=10,
            help="Cement slurry density"
        )
        
        plug_bottom_depth = st.number_input(
            "Plug Bottom Depth (m)",
            min_value=0.0,
            max_value=10000.0,
            value=1000.0,
            step=50.0,
            help="Bottom of cement plug"
        )
    
    # Design parameters based on plug type
    if plug_type == "Abandonment (P&A)":
        st.info("🟢 P&A Plug - High quality, permanent seal required")
        recommended_density = 1900
        excess_recommended = 0.20
    elif plug_type == "Sidetrack":
        st.info("🟡 Sidetrack Plug - Hard plug needed for kicking off")
        recommended_density = 1950
        excess_recommended = 0.15
    else:  # Well Suspension
        st.info("🔵 Suspension Plug - Temporary seal")
        recommended_density = 1850
        excess_recommended = 0.15
    
    if st.button("🔨 Design Plug", type="primary"):
        try:
            # Validate inputs
            if plug_bottom_depth <= plug_top_depth:
                st.error("❌ Bottom depth must be greater than top depth!")
                st.stop()
            
            if hole_diameter_plug <= 0:
                st.error("❌ Hole diameter must be positive!")
                st.stop()
            
            plug_length = plug_bottom_depth - plug_top_depth
            
            # Calculate volumes
            plug_volume = (np.pi / 4) * (hole_diameter_plug**2) * plug_length
            excess_volume = plug_volume * excess_recommended
            total_volume = plug_volume + excess_volume
            contamination_volume = plug_volume * 0.10  # 10% contamination allowance
            
            # Displacement volume
            displacement_volume = total_volume * 0.5
            
            # Save to session state
            st.session_state.plug_designed = True
            st.session_state.plug_design = {
                'type': plug_type,
                'length': plug_length,
                'volume': plug_volume,
                'total_volume': total_volume,
                'density': plug_density,
                'top_depth': plug_top_depth,
                'bottom_depth': plug_bottom_depth
            }
            
            # ---------- DISPLAY RESULTS ----------
            st.markdown("---")
            st.subheader("📊 Plug Design Results")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Plug Type", plug_type)
                st.metric("Plug Length", f"{plug_length:.1f} m")
            with col2:
                st.metric("Cement Volume", f"{plug_volume:.2f} m³")
                st.metric("Total Volume (with excess)", f"{total_volume:.2f} m³")
            with col3:
                st.metric("Slurry Density", f"{plug_density:.0f} kg/m³")
                st.metric("Displacement Volume", f"{displacement_volume:.2f} m³")
            
            # ---------- DETAILED BREAKDOWN ----------
            st.markdown("---")
            st.subheader("📋 Detailed Breakdown")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Volume Components:**")
                st.write(f"- Cement Volume: {plug_volume:.2f} m³")
                st.write(f"- Excess Volume ({excess_recommended*100:.0f}%): {excess_volume:.2f} m³")
                st.write(f"- Contamination Allowance: {contamination_volume:.2f} m³")
            with col2:
                st.write("**Recommended Parameters:**")
                st.write(f"- Recommended Density: {recommended_density} kg/m³")
                st.write(f"- Recommended Excess: {excess_recommended*100:.0f}%")
                st.write(f"- Required Displacement: {displacement_volume:.2f} m³")
            
            # ---------- INTEGRITY CHECK ----------
            st.markdown("---")
            st.subheader("✅ Plug Integrity Check")
            
            formation_pressure = st.number_input(
                "Formation Pressure at Plug Depth (MPa)",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=0.5,
                help="Expected formation pressure at plug depth"
            )
            
            # Calculate hydrostatic pressure of cement
            gravity = 9.81
            cement_hydrostatic = plug_density * gravity * plug_bottom_depth / 1e6
            overbalance = cement_hydrostatic - formation_pressure
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cement Hydrostatic", f"{cement_hydrostatic:.2f} MPa")
            with col2:
                st.metric("Formation Pressure", f"{formation_pressure:.2f} MPa")
            with col3:
                st.metric("Overbalance", f"{overbalance:.2f} MPa")
            
            if overbalance > 1.0:
                st.success(f"✅ Plug integrity verified!")
                st.info(f"Overbalance of {overbalance:.2f} MPa is adequate")
            elif overbalance > 0:
                st.warning(f"⚠️ Marginal overbalance: {overbalance:.2f} MPa")
                st.info("Consider increasing cement density")
            else:
                st.error(f"❌ Insufficient overbalance!")
                st.error(f"Overbalance is {overbalance:.2f} MPa")
                st.warning("⚠️ Formation pressure exceeds cement hydrostatic!")
                st.warning("Increase cement density or use a deeper plug")
            
            # ---------- RECOMMENDATIONS ----------
            st.markdown("---")
            st.subheader("💡 Recommendations")
            
            if plug_type == "Abandonment (P&A)":
                st.info("📌 Use high-strength Class G or H cement")
                st.info("📌 Include retarder for deep wells")
                st.info("📌 Ensure 20% excess for safety")
                st.info("📌 Wait 24-48 hours for full strength")
            elif plug_type == "Sidetrack":
                st.info("📌 Use high-density cement (1950+ kg/m³)")
                st.info("📌 Add silica flour for hardness")
                st.info("📌 Consider including weighting agents")
                st.info("📌 Wait 12-24 hours before sidetracking")
            else:  # Well Suspension
                st.info("📌 Use standard Class A or G cement")
                st.info("📌 Include 15% excess")
                st.info("📌 Good for short-term suspension (1-6 months)")
                st.info("📌 Test plug integrity before suspending")
            
            st.success(f"✅ {plug_type} plug designed successfully!")
            
        except Exception as e:
            st.error(f"❌ Error in plug design: {str(e)}")
            st.info("Please check your inputs and try again.")


# ============================================
# PAGE 7: PRESSURE PROFILE
# ============================================
elif page == "📊 Pressure Profile":
    st.header("📊 Pressure Profile Analysis")
    st.markdown("Visualize mud pressure vs pore and fracture pressure")
    
    st.info("""
    **Safe Drilling Window:**
    - Mud pressure should be **ABOVE** pore pressure (to prevent kicks)
    - Mud pressure should be **BELOW** fracture pressure (to prevent lost circulation)
    - The green area shows the safe zone!
    """)
    
    # ---------- INPUT SECTION ----------
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Well Data")
        
        # Well depth range
        top_depth = st.number_input(
            "Top Depth (m)",
            min_value=0.0,
            max_value=10000.0,
            value=0.0,
            step=100.0,
            help="Shallowest depth to analyze"
        )
        
        bottom_depth = st.number_input(
            "Bottom Depth (m)",
            min_value=100.0,
            max_value=10000.0,
            value=3000.0,
            step=100.0,
            help="Deepest depth to analyze"
        )
        
        num_points = st.slider(
            "Number of Data Points",
            min_value=10,
            max_value=100,
            value=50,
            step=5,
            help="How many points to plot (higher = smoother curve)"
        )
    
    with col2:
        st.subheader("Pressure Data")
        
        # Get mud density from session state if available
        default_mud_density = 1200.0
        if 'mud_properties' in st.session_state:
            default_mud_density = st.session_state.mud_properties.get('mud_weight', 1200.0)
        
        mud_density = st.number_input(
            "Mud Density (kg/m³)",
            min_value=800.0,
            max_value=3000.0,
            value=default_mud_density,
            step=10.0,
            help="Current drilling fluid density"
        )
        
        # Pore pressure gradient (normal = 10.5 kPa/m)
        pore_gradient = st.number_input(
            "Pore Pressure Gradient (kPa/m)",
            min_value=5.0,
            max_value=25.0,
            value=10.5,
            step=0.5,
            help="Normal pore pressure gradient is ~10.5 kPa/m"
        )
        
        # Fracture pressure gradient (typically 15-20 kPa/m)
        fracture_gradient = st.number_input(
            "Fracture Pressure Gradient (kPa/m)",
            min_value=10.0,
            max_value=30.0,
            value=18.0,
            step=0.5,
            help="Typical fracture gradient: 15-20 kPa/m"
        )
    
    # ---------- CALCULATE AND PLOT ----------
    if st.button("📊 Generate Pressure Profile", type="primary"):
        try:
            # Validate inputs
            if bottom_depth <= top_depth:
                st.error("❌ Bottom depth must be greater than top depth!")
                st.stop()
            
            if mud_density <= 0:
                st.error("❌ Mud density must be positive!")
                st.stop()
            
            # Generate depth points
            depths = np.linspace(top_depth, bottom_depth, num_points)
            
            # Calculate pressures
            gravity = 9.81
            
            # 1. Mud Pressure (Hydrostatic)
            mud_pressure = mud_density * gravity * depths / 1000  # Convert to kPa
            
            # 2. Pore Pressure
            pore_pressure = pore_gradient * depths  # kPa
            
            # 3. Fracture Pressure
            fracture_pressure = fracture_gradient * depths  # kPa
            
            # ---------- CREATE THE PLOT ----------
            fig = go.Figure()
            
            # Add Mud Pressure (Blue line)
            fig.add_trace(go.Scatter(
                x=mud_pressure,
                y=depths,
                mode='lines',
                name='Mud Pressure',
                line=dict(color='blue', width=3),
                hovertemplate='Depth: %{y:.0f} m<br>Pressure: %{x:.1f} kPa<extra></extra>'
            ))
            
            # Add Pore Pressure (Red line)
            fig.add_trace(go.Scatter(
                x=pore_pressure,
                y=depths,
                mode='lines',
                name='Pore Pressure',
                line=dict(color='red', width=3, dash='dash'),
                hovertemplate='Depth: %{y:.0f} m<br>Pressure: %{x:.1f} kPa<extra></extra>'
            ))
            
            # Add Fracture Pressure (Orange line)
            fig.add_trace(go.Scatter(
                x=fracture_pressure,
                y=depths,
                mode='lines',
                name='Fracture Pressure',
                line=dict(color='orange', width=3, dash='dot'),
                hovertemplate='Depth: %{y:.0f} m<br>Pressure: %{x:.1f} kPa<extra></extra>'
            ))
            
            # Add Safe Zone (Green fill between pore and fracture)
            fig.add_trace(go.Scatter(
                x=fracture_pressure,
                y=depths,
                mode='lines',
                name='Safe Zone',
                line=dict(width=0),
                showlegend=False
            ))
            
            fig.add_trace(go.Scatter(
                x=pore_pressure,
                y=depths,
                mode='lines',
                name='Safe Zone Fill',
                fill='tonexty',
                fillcolor='rgba(0, 255, 0, 0.2)',
                line=dict(width=0),
                showlegend=False
            ))
            
            # Update layout
            fig.update_layout(
                title={
                    'text': 'Pressure Profile - Safe Drilling Window',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                xaxis_title='Pressure (kPa)',
                yaxis_title='Depth (m)',
                yaxis=dict(
                    autorange='reversed',
                    gridcolor='lightgray'
                ),
                xaxis=dict(
                    gridcolor='lightgray'
                ),
                hovermode='y unified',
                legend=dict(
                    x=0.02,
                    y=0.98,
                    bgcolor='rgba(255, 255, 255, 0.8)'
                ),
                height=600,
                plot_bgcolor='white'
            )
            
            # Display the plot
            st.plotly_chart(fig, use_container_width=True)
            
            # ---------- SAFETY ANALYSIS ----------
            st.markdown("---")
            st.subheader("🔍 Safety Analysis")
            
            # Check mud pressure at bottom
            mud_at_bottom = mud_pressure[-1]
            pore_at_bottom = pore_pressure[-1]
            frac_at_bottom = fracture_pressure[-1]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Mud Pressure at Bottom", f"{mud_at_bottom:.1f} kPa")
                if mud_at_bottom > pore_at_bottom:
                    st.success("✅ Above pore pressure")
                else:
                    st.error("❌ Below pore pressure - KICK RISK!")
            
            with col2:
                st.metric("Pore Pressure at Bottom", f"{pore_at_bottom:.1f} kPa")
                status = "Normal" if pore_at_bottom < 15000 else "High"
                st.info(f"ℹ️ {status} pressure zone")
            
            with col3:
                st.metric("Fracture Pressure at Bottom", f"{frac_at_bottom:.1f} kPa")
                if mud_at_bottom < frac_at_bottom:
                    st.success("✅ Below fracture pressure")
                else:
                    st.error("❌ Above fracture pressure - LOST CIRCULATION RISK!")
            
            # ---------- OVERALL SAFETY STATUS ----------
            st.markdown("---")
            
            # Determine overall safety
            if mud_at_bottom > pore_at_bottom and mud_at_bottom < frac_at_bottom:
                st.success("✅ **SAFE DRILLING WINDOW**")
                st.success(f"Mud pressure ({mud_at_bottom:.1f} kPa) is between pore pressure ({pore_at_bottom:.1f} kPa) and fracture pressure ({frac_at_bottom:.1f} kPa)")
                
                # Calculate safety margins
                margin_to_pore = mud_at_bottom - pore_at_bottom
                margin_to_frac = frac_at_bottom - mud_at_bottom
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Overbalance (vs Pore)", f"{margin_to_pore:.1f} kPa", delta="Safe")
                with col2:
                    st.metric("Underbalance (vs Fracture)", f"{margin_to_frac:.1f} kPa", delta="Safe")
                    
            elif mud_at_bottom <= pore_at_bottom:
                st.error("❌ **KICK RISK DETECTED!**")
                st.error(f"Mud pressure ({mud_at_bottom:.1f} kPa) is BELOW pore pressure ({pore_at_bottom:.1f} kPa)")
                st.warning("⚠️ Increase mud weight to prevent kick!")
                st.info(f"Recommended mud density: {(pore_at_bottom / (gravity * bottom_depth / 1000) + 10):.0f} kg/m³")
                
            else:  # mud_at_bottom >= frac_at_bottom
                st.error("❌ **LOST CIRCULATION RISK DETECTED!**")
                st.error(f"Mud pressure ({mud_at_bottom:.1f} kPa) is ABOVE fracture pressure ({frac_at_bottom:.1f} kPa)")
                st.warning("⚠️ Decrease mud weight or set casing deeper!")
                st.info(f"Maximum allowed mud density: {(frac_at_bottom / (gravity * bottom_depth / 1000) - 10):.0f} kg/m³")
            
            # Mark as checked
            st.session_state.pressure_checked = True
            
            # ---------- DETAILED DATA TABLE ----------
            with st.expander("📋 View Detailed Pressure Data"):
                # Create a summary table
                data_table = pd.DataFrame({
                    'Depth (m)': depths,
                    'Mud Pressure (kPa)': mud_pressure,
                    'Pore Pressure (kPa)': pore_pressure,
                    'Fracture Pressure (kPa)': fracture_pressure,
                    'Status': [
                        "✅ Safe" if p > pore and p < frac else "❌ Unsafe" 
                        for p, pore, frac in zip(mud_pressure, pore_pressure, fracture_pressure)
                    ]
                })
                st.dataframe(data_table, use_container_width=True)
                
                # Download button for data
                csv = data_table.to_csv(index=False)
                st.download_button(
                    label="📥 Download Pressure Data (CSV)",
                    data=csv,
                    file_name="pressure_profile_data.csv",
                    mime="text/csv"
                )
            
            st.success("✅ Pressure profile generated successfully!")
            
        except Exception as e:
            st.error(f"❌ Error generating pressure profile: {str(e)}")
            st.info("Please check your inputs and try again.")


# ========== FOOTER ==========
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **PyMudCement-Optima v2.1**
    
    Developed for PENG 258
    Drilling Engineering 1
    
    © 2026 DPNGE-UENR
    
    **Features:**
    ✅ Drilling Fluids
    ✅ Mud Formulation (NEW!)
    ✅ Rheology Analysis
    ✅ Cementing Design
    ✅ Plug & Abandonment
    ✅ Pressure Profile
    ✅ Error Handling
    """
)

# Display version info
st.sidebar.markdown("---")
st.sidebar.caption("Version 2.1 | Updated July 2026")